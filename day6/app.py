from flask import Flask, render_template,request,redirect,url_for
import pip._vendor.requests as requests

app = Flask(__name__)

@app.route('/')
def index():
    namesList = ["Solomon","Hari", "Bob"]
    return render_template('index.html', names = namesList)

@app.route("/insert", methods=['POST'])
def insert():
    return render_template("insert.html")

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)