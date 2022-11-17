from atexit import register
from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask import flash


class Users:
    def __init__(self,data:dict):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = data['password']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.posts = []

    @staticmethod
    def validate_register(form_data:dict):
        register_valid = True
        is_valid_email = True
        if len(form_data.get('first_name')) <= 2:
            flash('First name requires at least 2 characters.', 'register')
            register_valid = False
        if len(form_data.get('last_name')) <= 2:
            flash('Last name requires at least 2 characters.', 'register')
            register_valid = False
        if len(form_data.get('email')) <= 0:
            flash('Email is required.', 'register')
            register_valid = False
            is_valid_email = False
        if not EMAIL_REGEX.match(form_data.get('email')):
            flash("Invalid email!", 'register')
            register_valid = False
            is_valid_email = False
        if is_valid_email:
            query = "SELECT * FROM users WHERE email = %(email)s;"
            results = connectToMySQL('cd_wall').query_db(query, {'email':form_data.get('email')})
        if len(results) >= 1:
            flash("Email already taken.", 'register')
            register_valid = False
        if len(form_data.get('password')) <= 8:
            flash('Password must at least have 8 characters.', 'register')
            register_valid = False
        if form_data.get('password') != form_data.get('confirm_password'):
            flash('Passwords must match!', 'register')
            register_valid = False
        return register_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('cd_wall').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data:dict):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL('cd_wall').query_db(query, data)
        return results

    @classmethod
    def select_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('cd_wall').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('cd_wall').query_db(query, data)
        return cls(results[0])
