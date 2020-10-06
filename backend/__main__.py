from flask import Flask

from flask import jsonify 
from flask import request 

from chatbot.model_prediction import *

app = Flask(__name__)

@app.route("/conv", methods=["GET"])
def conv():
    sentence = request.args["sentence"]
    response = predict(sentence)
    return jsonify(response)

@app.route("/status", methods=["GET"])
def status():
    return jsonify(True)

if("__main__" == __name__):
    app.run()
