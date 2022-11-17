from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.user import Users
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/create', methods = ['POST'])
def create_recipe():
    recipe_valid = Recipe.is_valid(request.form)
    if recipe_valid:
        Recipe.save_recipe(request.form)
        return redirect('/dashboard')
    return redirect('/recipes/new')

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/show/<int:recipe_id>')
def show_recipe(recipe_id):
    user = Users.get_by_id(session['user_id'])
    recipe = Recipe.get_by_id(recipe_id)
    return render_template("show_recipe.html", user=user, recipe=recipe)

@app.route('/edit/<int:recipe_id>')
def edit(recipe_id):
    recipe=Recipe.get_by_id(recipe_id)
    return render_template("edit_recipe.html", recipe=recipe)

@app.route('/update/<int:recipe_id>', methods = ["POST"])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/')
    recipe_valid = Recipe.is_valid(request.form)
    if not recipe_valid:
        return redirect(f'/recipes/edit/{{recipe_id}}')
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

@app.route('/destroy/<int:recipe_id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')