from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import order

class Favourite:
    db_name = "pizza_time_3"

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.order_id = data['order_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO favourite (user_id, order_id) VALUES(%(user_id)s, %(order_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_by_user_id(cls,data):
        query = "SELECT * FROM favourite WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        items = []
        for row in results:
            items.append(row)
        return items
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM favourite WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)