from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')           
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order = {
        'firstname': request.form['first_name'],
        'lastname': request.form['last_name'],
        'studentid': request.form['student_id'],
        'strawberry': request.form['strawberry'],
        'raspberry': request.form['raspberry'],
        'apple': request.form['apple']
    }
    return render_template("checkout.html", order=order)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)      