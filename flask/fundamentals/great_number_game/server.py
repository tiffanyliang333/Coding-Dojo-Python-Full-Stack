from flask import Flask, render_template, session, redirect, request
import random 
random.randint(1, 100)


app=Flask(__name__)

app.secret_key = "abcde"

@app.route('/')
def index():
    if "guess" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)
