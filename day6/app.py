from flask import Flask, render_template,request,redirect,url_for
import pip._vendor.requests as requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    namesList = ["Solomon","Hari", "Bob"]
    return render_template('index.html', names = namesList)

@app.route("/insert", methods=['POST'])
def insert():
    name = request.form["name"]
    place = request.form["place"]
    details = {
        "name":name,
        "place":place
    }
    with open('data.json','w') as f:
        json_data = json.dumps(details)
        f.write(json_data)
    return render_template("insert.html", userName = name, userPlace = place)

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)