# app.py
from utils.question import generate_question
from flask import Flask, render_template, request
import json
from os import listdir
import sys
sys.path.append('src/')

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'])
def index():
    csv_list = listdir("src/data")

    return render_template("index.html", csv_list=sorted(csv_list, key=len))


@app.route("/exam/<selectFileName>", methods=['GET'])
def exam(selectFileName):
    data = generate_question(selectFileName)
    return render_template("exam.html", selectFileName=selectFileName, questionList=data[0], answerList=data[1])


@app.route("/review/<selectFileName>", methods=['GET'])
def review(selectFileName):
    data = generate_question(selectFileName)
    return render_template("review.html", selectFileName=selectFileName, questionList=data[0], answerList=data[1])


if __name__ == "__main__":
    app.run(debug=True)
