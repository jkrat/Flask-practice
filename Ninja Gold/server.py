from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)  
app.secret_key = 'dortmund'

def find_luck():
    luck = random.random()
    return luck

def decide_win_or_lose():
    chances = random.randint(0, 1)
        return chances == 1



@app.route('/')           
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template("index.html", gold=session['gold'], activity=session['activity'])

@app.route('/process_money', methods=["POST"])
def calc_gold():
    luck = random.random()
    if request.form('property') == 'Farm':
        session['gold'] += (luck * 10 + 10)
    elif request.form('property') == 'Cave':
        session['gold'] += (luck * 5 + 5)
    elif request.form('property') == 'House':
        session['gold'] += (luck * 3 + 2)
    elif request.form('property') == 'Casino':
        win_chance = randon.randint(0,1)
        if win_chance == 0:
            session['gold'] + (luck * 50)
        else:
            session['gold'] - (luck * 50)

    return redirect('/')

@app.route('/reset', methods=["GET"])
def reset():
    session.pop('number')  #OR session['count] = 0 OR session.clear() 
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)      