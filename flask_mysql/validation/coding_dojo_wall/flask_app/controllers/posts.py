from flask import render_template, redirect, request, session, flash

from flask_app import app, bcrypt

from flask_app.models.user import Users
from flask_app.models.post import Posts

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/create_post', methods =["POST"])
def createPost():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "content": request.form["content"],
        "user_id": request.form["user_id"]
    }
    if len(data['content']) < 1:
        flash('Post content must not be blank.', 'content')
        return redirect('/wall')
    Posts.save_post(data)
    return redirect('/wall')

@app.route('/destroy/post/<int:id>')
def destroy_post(id):
    data = {
        "id":id
    }
    Posts.destroy(data)
    return redirect('/wall')