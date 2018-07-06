from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def create_default_board():
    COLORS = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    COLORS2 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    return render_template("index.html", x=8, y=8, colors=COLORS, colors2=COLORS2)

@app.route("/<x>/<y>")
def create_custom_board(x, y):
    x = int(x)
    y = int(y)
    COLORS = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    COLORS2 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    return render_template("index.html", x=x, y=y, colors=COLORS, colors2=COLORS2)

if __name__=="__main__":
    app.run(debug=True)