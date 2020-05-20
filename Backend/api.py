
from click.testing import CliRunner
from json import dumps
from flask import Flask, jsonify, request, Response
import sys
import os
sys.path.append(
    "F:\CNTT\CNTT_8\Khai Pha Web\BTL\Keyword_extraction_yake\Backend\Module")
from Module.yake import highlight
from Module.yake import yake
app = Flask(__name__)


@app.route("/api/home", methods=["POST", "GET"])
def get_text():
    if request.method == 'POST':
        text = request.json.get('text')
        lan = request.json.get('lan')
        ngram = request.json.get('ngram')
        feauture = request.json.get('feauture')
        numofwords = request.json.get('numOfKeyWords')

        # yake is here
        keywords = yake.KeywordExtractor(lan=lan, n=ngram, top=numofwords)
        resultWords = keywords.extract_keywords(text)

        th = highlight.TextHighlighter(max_ngram_size=ngram)
        text_hg = th.highlight(text, resultWords)
        print(text_hg)

        array = []
        for i in resultWords:
            arr = {}
            arr["word"] = i[0]
            arr["score"] = i[1]
            array.append(arr)

        print(resultWords)
        result = {}
        result['text'] = text_hg
        result['result'] = array
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
