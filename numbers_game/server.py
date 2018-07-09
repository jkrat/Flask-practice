from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = 'dortmund'

@app.route('/')           
def index():
    session['number'] = random.randint(0, 100)
    box_class = "hidden"
    button_class = "hidden"
    print(session['number'])
    return render_template("index.html", box_class=box_class, button_class=button_class)

@app.route('/guess', methods=["POST"])
def guess():
    guess_num = request.form['guess']
    if int(guess_num) == session['number']:
        box_class = "green"
        submit_class = "hidden"
        button_class = ""
        user_feedback = f"{guess_num} was the number!"
    elif int(guess_num) > session['number']:
        box_class = "red" 
        user_feedback = "Too high!"
        button_class = "hidden"
        submit_class = ""
    elif int(guess_num) < session['number']:
        box_class = "red" 
        user_feedback = "Too low!"
        button_class = "hidden"
        submit_class = ""
    return render_template("index.html", box_class=box_class, user_feedback=user_feedback, button_class=button_class, submit_class=submit_class)

@app.route('/reset', methods=["GET"])
def reset():
    session.pop('number')  #OR session['count] = 0 OR session.clear() 
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)      