from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_mysql.crud.dojos_and_ninjas.flask_app.controllers.dojos import dojo_with_ninjas

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        ninjas = []
        for n in results:
            ninjas.append( cls(n))
        return ninjas

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result

    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)