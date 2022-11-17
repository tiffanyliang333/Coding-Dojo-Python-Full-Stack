from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save_dojos(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_with_ninjas(id):
    data = {
        "id":id
    }
    return render_template('dojos.html', dojo=Dojo.get_dojo_with_ninjas(data))