"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Semis(Controller):
    def __init__(self, action):
        super(Semis, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Semi')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        display_products=self.models['Semi'].get_prs()
        return self.load_view('index.html', display=display_products)


    def create(self):
        pr_info={
            'name':request.form['name'],
            'description':request.form['description'],
            'price':request.form['price']
        }
        pr= self.models['Semi'].create_a_pr(pr_info)
        return redirect('/')

    def show(self, id):
        
        result=self.models['Semi'].show_pr(id)
  
        return self.load_view('/show.html', show_product=result)

    def edit(self, id):
        edit_result=self.models['Semi'].edit_pr(id)

        return self.load_view('/edit.html',edit_product=edit_result[0])

    def update(self):
        print "HI i am c imuk9i65hhrhh63g53"
        update_info={
            'id':request.form['pr_id'],
            'name':request.form['name'],
            'description':request.form['description'],
            'price':request.form['price']   
        }
        print update_info
      
        update_result=self.models['Semi'].update_pr(update_info)

        return redirect('/')
    def destroy(self,id):
        destroy_result=self.models['Semi'].destroy_pr(id)
        return redirect('/')
