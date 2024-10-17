import uuid
from datetime import datetime
from app.models.basemodel import BaseModel

class User(BaseModel):
    """"""
    def __init__(self) -> None:
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.is_admin = False

        pass

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