from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja  # ou from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos = []
        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # comes back as the new row id
        result = connectToMySQL('dojo_ninja').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojo_ninja').query_db(query,data)
        return cls(result[0])
    

    @classmethod
    def get_dojo_with_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja').query_db(query, data )
    # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls(results[0])
        for row_from_db in results:
 
 # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
            "id": row_from_db["ninjas.id"],
            "first_name": row_from_db['first_name'],
            "last_name": row_from_db['last_name'],
            "age": row_from_db['age'],
            "created_at": row_from_db['ninjas.created_at'],
            "updated_at": row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo


    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninja').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninja').query_db(query,data)
