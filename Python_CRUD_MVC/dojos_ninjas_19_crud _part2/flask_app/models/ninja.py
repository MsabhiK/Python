from flask_app.config.mysqlconnection import connectToMySQL
#from .dojo import Dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        #self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        ninjas = []
        for n in results:
            ninjas.append( cls(n) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"

        # comes back as the new row id
        result = connectToMySQL('dojo_ninja').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,id):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL('dojo_ninja').query_db(query,data)
        ninja = cls(result[0])
        return ninja

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninja').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {
            "id": id
        }
        return connectToMySQL('dojo_ninja').query_db(query,data)