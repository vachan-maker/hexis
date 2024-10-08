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
    data = []
    with engine.connect() as connection:
        results = connection.execute(text("""
        SELECT * FROM details
"""))
        for row in results:
            data.append({"name":row[0], "place":row[1]})
    return data

@app.route('/sabumon')
def sabumon():
    data = []
    with engine.connect() as connection:
        results = connection.execute(text("""
        SELECT * FROM details WHERE name CONTAINS 'Sabu'
"""))
        for row in results:
            data.append({"name":row[0], "place":row[1]})
    return data

@app.route("/insert", methods=['POST'])
def insert():
    name = request.form["name"]
    place = request.form["place"]
    details = {
        "name":name,
        "place":place
    }
    print("before database connection")
    with engine.connect() as connection:
        result = connection.execute(text("""
            INSERT INTO details (name, place) VALUES (:name, :place)
        """), {"name": name, "place": place})
        connection.commit() 
    return render_template("insert.html", userName=name, userPlace=place)


@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)