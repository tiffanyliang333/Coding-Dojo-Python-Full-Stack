from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.cookie import Cookie_order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookie_summary():
    return render_template('cookies.html', cookies=Cookie_order.get_all())

@app.route('/cookies/new')
def new():
    return render_template('new_cookie.html')

@app.route('/cookies/create', methods = ['POST'])
def create_order():
    if Cookie_order.validate_order(request.form) == True:
        print(request.form)
        Cookie_order.save(request.form)
        return redirect('/cookies')
    else:
        print('not valid')
        return redirect('/cookies/new')

@app.route('/cookies/edit/<int:id>')
def edit_order(id):
    data = {
        "id":id
    }
    return render_template('edit_order.html', cookie=Cookie_order.get_one(data))

@app.route('/cookies/update', methods = ['POST'])
def update():
    if Cookie_order.validate_order(request.form) == True:
        Cookie_order.update(request.form)
        return redirect('/')
    else:
        return redirect(f'/cookies/edit/{request.form["id"]}')