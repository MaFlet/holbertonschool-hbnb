import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
    self.id = str(uuid.uuid4())
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.is_admin = False
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
