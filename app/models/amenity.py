import uuid
from datetime import datetime

class Amenity(Place):
    def __init__(self, id, name):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
