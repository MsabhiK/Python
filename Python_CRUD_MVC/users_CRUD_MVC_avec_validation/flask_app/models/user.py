from flask_app.config.mysqlconnection import connectToMySQL
# Etape 2 for validation: from flask import flash, import re et  EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    DB = "users_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #self.classroom = None

#READ ALL DATA  #### ONE TO MANY: classrooms to users ###
    @classmethod
    def get_all(cls):
        #query = "SELECT * FROM users LEFT JOIN classrooms ON users.classroom_id = classrooms.id;"
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)

        if results == []:
            return []
        users = []
        for row in results:
            user = cls(row)
           
            #classroom_data = {
             #   'id': row['classrooms.id'],
              #  'name': row['name'],
               # 'description': row['description'],
                #'created_at': row['classrooms.created_at'],
                #'updated_at': row['classrooms.updated_at']
            #}
            #user.classroom = Classroom(classroom_data)
         
            users.append(user)
        return users
    
#READ ONE DATA BY ID  #### ONE TO MANY: classrooms to users ###
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    """
    def get_one(cls, data):
        query  = "SELECT * FROM users LEFT JOIN classrooms ON users.classroom_id = classrooms.id WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)

        if result == []:
            return None
        user = cls(result[0])
      
        classroom_data = {
                'id': result[0]['classrooms.id'],
                'name': result[0]['name'],
                'description': result[0]['description'],
                'created_at': result[0]['classrooms.created_at'],
                'updated_at': result[0]['classrooms.updated_at']
            }
        user.classroom = Classroom(classroom_data)
        
        return user
        """
    
#CREATE OR ADDING ROW IN DATA
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.DB).query_db(query, data)
    
#UPDATE OR EDIT DATA BY ID
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
#DELETE DATA BY ID
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    #etape 1 for validation
    @staticmethod
    def validate_users(users):
        is_valid = True # we assume this is true
        if not users['fname']:
          flash("First_Name cannot be blank!", 'first_name')
          is_valid = False
        if len(users['fname']) < 3:
            flash("first_name must be at least 3 characters.")
            is_valid = False
        if not users['lname']:
            flash("last_Name cannot be blank!", 'last_name')
            is_valid = False
        if len(users['lname']) < 3:
            flash("last_name must be at least 3 characters.")
            is_valid = False
        if not users['email']:
            flash("Email cannot be blank!", 'email')
            is_valid = False
        if not EMAIL_REGEX.match(users['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid