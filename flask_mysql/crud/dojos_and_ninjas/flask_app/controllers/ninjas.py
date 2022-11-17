from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def new_ninjas():
    return render_template("ninjas.html", dojos= Dojo.get_all_dojos())

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.save_ninja(request.form)
    return redirect('/')

@app.route('/ninjas/edit/<int:id>')
def edit_ninja(id):
    data = {
        "id":id
    }
    return render_template(edit_ninja.html, ninja = Ninja.get_one_ninja(data))

@app.route('/ninjas/update', methods=['POST'])
def update():
    Ninja.update(request.form)
    return redirect('/')

@app.route('/ninjas/destroy/<int:id>')
def destroy(id):
    data={
        "id":id
    }
    Ninja.destroy(data)
    return redirect('/')