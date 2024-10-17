import uuid
from datetime import datetime

class Review(Place):
    def __init__(self, id, text, rating, place, user):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
