from app.models.basemodel import BaseModel

class User(BaseModel):
    """"""
    def __init__(self, f_name, l_name, i_email, admin=False) -> None:
        super.__init__()
        self.first_name = f_name
        self.last_name = l_name
        self.email = i_email
        self.is_admin = admin

        pass

    def update_email(self, newEmail):
        self.email = newEmail
        self.save()
# functions that can be put into the basemodel,
# if implemented.
#
#def save(self):
#   self.updated_at = datetime.now()
#
#def update(self, data):
#   for key, value in data.items()
#       if hasattr(self, key):
#           setattr(self,)