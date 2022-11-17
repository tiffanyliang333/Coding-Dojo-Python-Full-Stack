from atexit import register
from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.description = data.get('description')
        self.instructions = data.get('instructions')
        self.date_made = data.get('date_made')
        self.under_30 = data.get('under_30')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.user = None

    @staticmethod
    def is_valid(form_data):
        valid = True
        if len(form_data['name']) < 3:
            flash('Name must have at least 3 characters!')
            valid = False
        if len(form_data['description']) < 3:
            flash('Description must have at least 3 characters!')
            valid = False
        if len(form_data['instructions']) < 3:
            flash('Instructions must have at least 3 characters!')
            valid = False
        if len(form_data['date_made']) <= 0:
            flash('Date is required.')
            valid = False
        if "under_30" not in form_data:
            flash('Does you recipe take less than 30 minutes?')
            valid = False
        return valid

    @classmethod
    def get_user_recipes(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id=recipes.user_id;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def save_recipe(cls, form_data):
        if not cls.is_valid(form_data):
            return False
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
        results = connectToMySQL('recipes_schema').query_db(query,form_data)
        return results

    @classmethod
    def get_by_id(cls, recipe_id):
        data = {
            "id":recipe_id
        }
        query="SELECT recipes.id, name, description, instructions, date_made, under_30, recipes.created_at, recipes.updated_at, users.id as user_id, first_name, last_name, email, users.created_at, users.updated_at FROM recipes JOIN users on users.id=recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        result = cls(result[0])

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def destroy(cls,recipe_id):
        data = {"id":recipe_id}
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query,data)
        return recipe_id