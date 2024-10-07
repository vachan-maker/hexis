from flask import Flask, render_template,request,redirect,url_for;

app = Flask(__name__) #create instance/object of flask class

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)

@app.route('/name/<name>')
def name(name):
    return render_template('/templates/name.html', name=name)