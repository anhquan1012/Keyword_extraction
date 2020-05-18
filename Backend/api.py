import flask
import time
from flask import Flask, jsonify, request, Response
from json import dumps


app = Flask(__name__)


@app.route("/api/home", methods=["POST"])
def get_text():
    if request.method == 'POST':
        text = request.json.get('text')
        lan = request.json.get('lan')
        ngram = request.json.get('ngram')
        feauture = request.json.get('feauture')

        print(text, lan, ngram, feauture)
        # yake is here

        result = {}
        result['data'] = text
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
