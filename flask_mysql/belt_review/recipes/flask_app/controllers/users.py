from flask import render_template, redirect, request, session, flash

from flask_app import app, bcrypt

from flask_app.models.user import Users
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def r_login_registration():
    return render_template("index.html")

@app.route('/user/register', methods = ['POST'])
def register():
    if Users.validate_register(request.form):
        data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'password': bcrypt.generate_password_hash(request.form.get('password'))
        }
        id = Users.create_user(data)
        session['user_id'] = id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/user/login', methods = ['POST'])
def login():
    data={"email" : request.form["email"]}
    user_in_db = Users.select_email(data)
    if not user_in_db:
        flash("Invalid Email/Password!", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password!", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def r_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    return render_template("dashboard.html", user=Users.get_by_id(data), recipes=Recipe.get_user_recipes(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')