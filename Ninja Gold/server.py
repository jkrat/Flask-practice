from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)  
app.secret_key = 'dortmund'

def random_num(a, b):
    rnumber = random.randrange(a, b)
    return rnumber

def decide_win_or_lose():
    chances = random.randint(0, 1)
    return chances == 1
    
def add_activity(amount, action, property):
    timestamp = datetime.datetime.now()
    if property == 'Farm':
        session['activity'].append(['earn', f'Earned {amount} golds from the {property}! ({timestamp})'])
    if property == 'Cave':
        session['activity'].append(['earn', f'Earned {amount} golds from the {property}! ({timestamp})'])  
    if property == 'House':
        session['activity'].append(['earn', f'Earned {amount} golds from the {property}! ({timestamp})'])
    elif property == 'Casino':
        if action == 'earned':
            earned = f'Entered a casino and earned {amount} golds! ({timestamp})'
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = f'Entered a casino and lost {amount} golds... Ouch. ({timestamp})' 
            session['activity'].append(['lost', lost])

@app.route('/')           
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    print(session['gold'])
    print(session['activity'])
    return render_template("index.html", gold=session['gold'], activity_list=session['activity'])

@app.route('/process_money', methods=["POST"])
def calc_gold():
    property_name = request.form['property']
    if property_name == 'Farm':
        farm_number = random_num(10, 21)
        session['gold'] += farm_number
        add_activity(farm_number, 'earned', 'Farm')
    elif property_name == 'Cave':
        cave_number = random_num(5, 10)
        session['gold'] += cave_number
        add_activity(cave_number, 'earned', 'Cave')
    elif property_name == 'House':
        house_number = random_num(2, 5)
        session['gold'] += house_number
        add_activity(house_number, 'earned', 'House')
    elif property_name == 'Casino':
        casino_number = random_num(0, 50)
        chance = decide_win_or_lose()
        if chance == True:
            session['gold'] += casino_number
            add_activity(casino_number, 'earned', 'Casino')
        elif chance == False:
            session['gold'] -= casino_number
            add_activity(casino_number, 'lost', 'Casino')
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold'] = 0  #OR session['count'] = 0 OR session.clear() OR session.pop('')
    session['activity'] = []
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)      