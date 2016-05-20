""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Semi(Model):
    def __init__(self):
        super(Semi, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """
    def get_prs(self):
        query = "SELECT * from products"
        return self.db.query_db(query)

    def show_pr(self, info):
        query = "SELECT * from products where id_pr = :id"
        data={'id': info}
        ret=self.db.query_db(query,data)
        if not ret:
            return ret
        else:
            return ret[0]

    def create_a_pr(self, info):
        sql = "INSERT into products (name, description, price) values(:name,:description, :price)"
        data={
            'name':info['name'],
            'description':info['description'],
            'price':info['price']
        }
        added=self.db.query_db(sql, data)
        return added

    def edit_pr(self, info):

        query = "SELECT * from products where id_pr = :id"
        data={'id': info}
        return self.db.query_db(query,data)


    def update_pr(self, info):
        sql = "UPDATE products SET name=:name, description=:description, price=:price WHERE id_pr=:id"
        data={
            'id':info['id'],
            'name':info['name'],
            'description':info['description'],
            'price':info['price']
        }
        updated=self.db.query_db(sql, data)
        return updated

    def destroy_pr(self, info):
        query = "DELETE from products WHERE id_pr = :id"
        data={'id': info}
        return self.db.query_db(query,data)
    
    # def grab_messages(self):
    #     query = "SELECT * from messages where users_id = :user_id"
    #     data = {'user_id':1}
    #     return self.db.query_db(query, data)

