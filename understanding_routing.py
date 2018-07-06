from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/dojo")
def dojo():
    return "<h1>Dojo!</h1>"

@app.route("/say/<name>")
def say(name):
    return "<h1>Hi " + name + "!</h1>"

@app.route("/repeat/<num>/<word>")
def repeat(num, word):
    return "<h1>" + int(num) * (word + " ") + "</h>"


if __name__=="__main__":
    app.run(debug=True)