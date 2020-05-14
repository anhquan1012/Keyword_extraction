import flask
import time
from flask import Request, Flask

app = Flask(__name__)

@app.route("/home",methods = ["GET"])
def get_text():
    return {"time": time.time()}