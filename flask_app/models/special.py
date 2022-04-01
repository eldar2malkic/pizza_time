from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import order

class Special:
    db_name = "pizza_time_3"

    def __init__(self, data):
        self.id = data['id']
        self.method = data['method']
        self.size = data['size']
        self.crust = data['crust']
        self.quantity = data['quantity']
        self.topping = data['topping']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO specials (method, size, crust, quantity, topping, user_id) VALUES(%(method)s,%(size)s,%(crust)s,%(quantity)s, %(topping)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM specials;"
        results = connectToMySQL(cls.db_name).query_db(query)
        specials = []
        for row in results:
            specials.append(row)
        return specials

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM specials WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE specials SET method = %(method)s, size= %(size)s, crust= %(crust)s, quantity= %(quantity)s, topping= %(topping)s WHERE cart.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM specials WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)