import uuid
from datetime import datetime

class User():
    def __init__(self, first_name, last_name, email, is_admin=False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
        self.reviews = []

    