from flask import Flask, render_template,request,redirect,url_for
from sqlalchemy import create_engine, text
import pip._vendor.requests as requests
import json

app = Flask(__name__)
engine = create_engine("sqlite:///example.db")

with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS details (
            name VARCHAR(30),
            place VARCHAR(20)
        )
    """))


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