
from click.testing import CliRunner
from json import dumps
from flask import Flask, jsonify, request, Response
import sys
import os
import re
sys.path.append(
    "/home/luuthanh/Desktop/Keyword_extraction/Backend/Module")
from Module.yake import highlight
from Module.yake import yake
app = Flask(__name__)


# def pre_process(text):
    
#     # lowercase
#     text=text.lower()
    
#     #remove tags
#     text=re.sub("</?.*?>"," <> ",text)
    
#     # remove special characters and digits
#     text=re.sub("(\\d|\\W)+"," ",text)
    
#     return text


@app.route("/api/home", methods=["POST", "GET"])
def get_text():
    if request.method == 'POST':
        # print(request.json)
        text = request.json.get('text')
        # lan = request.json.get('lan')
        ngram = request.json.get('ngram')
        # feauture = request.json.get('feauture')
        numofwords = request.json.get('numOfKeyWords')

        # yake is here
        keywords = yake.KeywordExtractor(lan="vi", n=ngram , dedupLim=0.5, dedupFunc='jaro', windowsSize=1, top=numofwords)
        resultWords = keywords.extract_keywords(text)
        resultWords = [(k[0].replace("_"," "), round(k[1],5)) for k in resultWords]
        # print(resultWords)
        th = highlight.TextHighlighter(max_ngram_size=ngram)
        text_hg = th.highlight(text, resultWords)
        
        # word  = [w[0] for w in resultWords]

        # text = text.lower()
        # for i in word:
        #     text = text.replace(" {} ".format(i)," <mark>{}</mark> ".format(i))
        
        # print(text_hg)
        # word = [w[0].replace("_"," ") for w in resultWords]
        # for w in word:
        #     text = text.replace(w,'<mark>{}</mark>'.format(w))
        # print(word)
        # print(text)


        array = []
        for i in resultWords:
            arr = {}
            arr["word"] = i[0]
            arr["score"] = i[1]
            array.append(arr)

        # print(resultWords)
        result = {}
        result['text'] = text_hg
        result['result'] = array
        print(result['result'])
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
