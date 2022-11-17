# from atexit import register
# from flask_app import app
# from flask_app.config.mysqlconnection import connectToMySQL

# from flask import flash
# from flask_bcrypt import Bcrypt
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



# class Users:
#     def __init__(self,data:dict):
#         self.id = data.get('id')
#         self.first_name = data.get('first_name')
#         self.last_name = data.get('last_name')
#         self.email = data.get('email')
#         self.password = data['password']
#         self.created_at = data.get('created_at')
#         self.updated_at = data.get('updated_at')
#         # self.recipes = []

#     @staticmethod
#     def validate_register(form_data:dict):
#         register_valid = True
#         is_valid_email = True
#         if len(form_data.get('first_name')) <= 2:
#             flash('First name requires at least 2 characters.', 'register')
#             register_valid = False
#         if len(form_data.get('last_name')) <= 2:
#             flash('Last name requires at least 2 characters.', 'register')
#             register_valid = False
#         if len(form_data.get('email')) <= 0:
#             flash('Email is required.', 'register')
#             register_valid = False
#             is_valid_email = False
#         if not EMAIL_REGEX.match(form_data.get('email')):
#             flash("Invalid email!", 'register')
#             register_valid = False
#             is_valid_email = False
#         if is_valid_email:
#             query = "SELECT * FROM users WHERE email = %(email)s;"
#             results = connectToMySQL('recipes_schema').query_db(query, {'email':form_data.get('email')})
#             if len(results) >= 1:
#                 flash("Email already taken.", 'register')
#                 register_valid = False
#         if len(form_data.get('password')) <= 8:
#             flash('Password must at least have 8 characters.', 'register')
#             register_valid = False
#         if form_data.get('password') != form_data.get('confirm_password'):
#             flash('Passwords must match!', 'register')
#             register_valid = False
#         return register_valid

#     @classmethod
#     def create_user(cls, data:dict):
#         query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
#         results = connectToMySQL('recipes_schema').query_db(query, data)
#         return results

#     @classmethod
#     def get_by_id(cls, user_id):
#         data={"id":user_id}
#         query = "SELECT * FROM users WHERE id = %(id)s;"
#         results = connectToMySQL('recipes_schema').query_db(query, data)
#         return cls(results[0])

#     @classmethod
#     def select_email(cls, data):
#         # data = {"email": email}
#         query = "SELECT * FROM users WHERE email = %(email)s;"
#         results = connectToMySQL('recipes_schema').query_db(query, data)
#         if len(results) < 1:
#             return False
#         return cls(results[0])

#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('recipes_schema').query_db(query)
#         users = []
#         for user in results:
#             users.append(cls(user))
#         return users

#     @classmethod
#     def authenticated_user_by_input(cls, user_input):
#         valid=True
#         existing_user = cls.select_email(user_input['email'])
#         password_valid = True
#         if not existing_user:
#             valid=False
#         else:
#             password_valid = Bcrypt.check_password_hash(existing_user.password, user_input['password'])
#             if not password_valid:
#                 valid=False
#         if not valid:
#             flash("That email and password combination does nto match our records.")
#             return False
#         return existing_user

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import recipe
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DB = "recipes_schema"

class User:
    
    def __init__(self,user):

        self.id = user["id"]
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        # self.password=user['password']
        self.created_at = user["created_at"]
        self.updated_at = user["updated_at"]

    @classmethod
    def get_by_email(cls,email):

        data = {
            "email": email
        }
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls, user_id):

        data = {"id": user_id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        user_data = connectToMySQL(DB).query_db(query)

        users = []
        for user in user_data:
            users.append(cls(user))

        return users

    @classmethod
    # fetches an existing user after authenticating
    def authenticated_user_by_input(cls, user_input):
        
        valid = True
        existing_user = cls.get_by_email(user_input["email"])
        password_valid = True

        if not existing_user:
            valid = False
            
        else:
            password_valid = bcrypt.check_password_hash(
            existing_user.password, user_input['password'])
        
            if not password_valid:
                valid = False

        if not valid:
            flash("That email & password combination does not match our records.")
            return False

        return existing_user
    
    @classmethod
    def create_valid_user(cls, user):

        # Validate user
        if not cls.is_valid(user):
            return False

        # Hash password
        pw_hash = bcrypt.generate_password_hash(user['password'])
        user = user.copy()
        user["password"] = pw_hash
        print("User after adding pw: ", user)

        # Insert user into DB
        query = """
                INSERT into users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""

        new_user_id = connectToMySQL(DB).query_db(query, user)
        new_user = cls.get_by_id(new_user_id)

        return new_user

    @classmethod
    def is_valid(cls, user):
        valid = True

        if len(user["first_name"]) < 2:
            valid = False
            flash("First name must be at least 2 characters.")
        if len(user["last_name"]) < 2:
            valid = False
            flash("Last name must be at least 2 characters.") 
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            valid = False
        if not user["password"] == user["password_confirmation"]:
            flash("Did you have a typo? Passwords must match.")
            valid = False


        email_already_has_account = User.get_by_email(user["email"])
        if email_already_has_account:
            flash("An account with that email already exists, please log in.")
            valid = False

        return valid
    


    