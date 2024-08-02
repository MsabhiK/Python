from mysqlconnection import connectToMySQL
class User:
    DB = 'users_cr'
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

#### READ_ALL####        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
#### ADD_A_NEW_USER####"
    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

