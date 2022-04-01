from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Order:
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
        query = "INSERT INTO orders (method, size, crust, quantity, topping, user_id) VALUES(%(method)s,%(size)s,%(crust)s,%(quantity)s, %(topping)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results[0]

    @classmethod
    def get_by_user_id(cls,data):
        query = "SELECT * FROM orders WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        items = []
        for row in results:
            items.append(row)
        return items

    