from mysqlconnection import connectToMySQL

class User:
    DB ="users_cr"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#READ ALL DATA
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        
        results = connectToMySQL(cls.DB).query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users
    
#READ ONE DATA BY ID
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
#CREATE OR ADDING ROW IN DATA
    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.DB).query_db(query, data)
    
#UPDATE OR EDIT DATA BY ID
    @classmethod
    def update(cls,data):
        query = "UPDATE user SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
#DELETE DATA BY ID
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)