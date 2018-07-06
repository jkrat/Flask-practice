from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route("/play")
def render_for_play():   
    return render_template("index.html", times=3)

@app.route("/play/<x>")
def render_for_play_x(x):
    times = int(x)
    return render_template("index.html", times=times)

@app.route("/play/<x>/<color>")
def render_for_play_x_color(x, color):
    times = int(x)
    return render_template("index.html", times=times, color=color)

if __name__=="__main__":
    app.run(debug=True)