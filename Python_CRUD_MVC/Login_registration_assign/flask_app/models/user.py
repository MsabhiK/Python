from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL, DB
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.fullname = data['fullname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls , data):
        """
            data = {
                'fullname': value,
                'email': value,
                'password': value ("12345678")
            }
        """
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        # data's type is immutable => we cannot change it's value [immutableDictionary] => [Dictionary]
        data = dict(data)
        data['password'] = encrypted_password
        query = "INSERT INTO users (fullname, email, password) VALUES(%(fullname)s,%(email)s,%(password)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result == ():
            return None
        print("*"*100)
        print(result)
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        # If statements
        if len(data['fullname']) <= 7:
            is_valid = False
            flash("Full name must be at least 8 characters long.", "register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!", "register")
        if user_in_db:
            is_valid = False
            flash("EMAIL already registred!!!", "register")
        if not data['email']:
            is_valid = False
            flash("Email cannot be blank!", "register")
        if len(data['password']) <= 7:
            is_valid = False
            flash("Password must be at least 8 characters long.", "register")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords do not match.", "register")

        return is_valid
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            is_valid = False
            flash("Email Not Found!", "login")
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            is_valid = False
            flash("Incorrect Password!", "login")
        return is_valid
