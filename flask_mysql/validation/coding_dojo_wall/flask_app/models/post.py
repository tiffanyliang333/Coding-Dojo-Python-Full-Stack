from atexit import register
from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask_app.models import user

class Posts:
    def __init__(self, data):
        self.id = data.get('id')
        self.content = data.get('content')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.creator = None
    
    @classmethod
    def save_post(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s);"
        results = connectToMySQL('cd_wall').query_db(query,data)
        return results

    @classmethod
    def get_user_posts(cls, data):
        query = "SELECT * FROM posts JOIN users ON users.id=posts.user_id;"
        results = connectToMySQL('cd_wall').query_db(query,data)
        posts = []
        for post in results:
            posts.append(cls(post))
        return posts

    @classmethod
    def get_all_posts_with_creator(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id;"
        results = connectToMySQL('cd_wall').query_db(query)
        all_posts = []
        for row in results:
            one_post = cls(row)
            one_posts_author_info = {
                "id": row['user.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = user.Users(one_posts_author_info)
            one_post.creator = author
            all_posts.append(one_post)
        return all_posts

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        return connectToMySQL('cd_wall').query_db(query,data)