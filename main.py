from flask import Flask,request,render_template
#import requests
import random
#pip install flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/naloga1")
def coinflip():
    return render_template("naloga1.html")


@app.route("/Nal1")
def Nal1():




return render_template("Nal1.html")


app.run(debug = True)