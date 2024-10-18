import uuid
from datetime import datetime

class User():
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.is_admin = False
        self.created_at = datetime.now
        self.updated_at = datetime.now
        self.places = []
        pass