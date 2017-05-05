from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://r.ddmcdn.com/w_606/s_f/o_1/cx_0/cy_15/cw_606/ch_404/APL/uploads/2014/06/10-kitten-cuteness-1.jpg">
    """
    return html.format(name.title())

@app.route("/jedi/<firstname>/<lastname>")
def find_jedi_name(firstname, lastname):
    jedi_name = lastname[0:3] + firstname[0:2]
    return "Your Jedi name is {}.".format(jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
