from flask import Flask, flash, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'dortmund'

@app.route("/")
def user_form():   
    session['info'] = {}
    return render_template("index.html")

@app.route("/resut")
def info_page():     
    return render_template("result.html", info=session['info'])

@app.route("/submit", methods=["POST"])
def create_user():
    session['info'] = request.form

    if len(request.form['name']) < 1:
        flash('A name must be provided')
    if len(request.form['comment']) < 1:
        flash('A comment must be provided')
    if len(request.form['comment']) > 120:
        flash('A comment cannot have more than 120 characters')

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('result.html', info=session['info'])

@app.route("/danger")
def reroute_from_danger():
    print("a user tried to visit /danger")
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)  