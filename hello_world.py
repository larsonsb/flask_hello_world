from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello.html', my_name=name.title())

@app.route("/jedi/<firstname>/<lastname>")
def find_jedi_name(firstname, lastname):
    jedi_name = lastname[0:3] + firstname[0:2]
    return render_template('jedi.html', my_jedi_name=jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
