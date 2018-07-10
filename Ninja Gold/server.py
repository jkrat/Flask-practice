from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = 'dortmund'

@app.route('/')           
def index():
    
    return render_template("index.html", box_class=box_class, button_class=button_class)

@app.route('/guess', methods=["POST"])
def guess():

@app.route('/reset', methods=["GET"])
def reset():
    session.pop('number')  #OR session['count] = 0 OR session.clear() 
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)      