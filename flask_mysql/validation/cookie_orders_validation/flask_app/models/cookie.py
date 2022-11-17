from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Cookie_order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.cookie_box_qty = data['cookie_box_qty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_order(cookie_order):
        is_valid = True
        if len(cookie_order['customer_name']) <= 0 and len(cookie_order['cookie_type']) <= 0 and int(cookie_order['cookie_box_qty']) <= 0:
            flash("All fields required.")
            is_valid = False
            return is_valid
        if len(cookie_order['customer_name']) < 2:
            flash('Name must have at least 2 characters.')
            is_valid = False
        if len(cookie_order['cookie_type']) <= 0:
            flash('Cookie type must be specified.')
            is_valid = False
        if int(cookie_order['cookie_box_qty']) < 1:
            flash ('Please enter a valid box quantity.')
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_order;"
        results = connectToMySQL('cookies_schema').query_db(query)
        cookies = []
        for c in results:
            cookies.append( cls(c) )
        return cookies

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_order (customer_name, cookie_type, cookie_box_qty) VALUES (%(customer_name)s, %(cookie_type)s, %(cookie_box_qty)s);"
        results = connectToMySQL('cookies_schema').query_db(query, data)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookie_order WHERE id = %(id)s;"
        results = connectToMySQL('cookies_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE cookie_order SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, cookie_box_qty = %(cookie_box_qty)s WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query,data)