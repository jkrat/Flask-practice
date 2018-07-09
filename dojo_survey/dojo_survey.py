from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def user_form():   
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def create_user():
    info = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    return render_template("result.html", info = info)

if __name__=="__main__":
    app.run(debug=True)  