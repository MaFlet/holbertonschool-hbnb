import uuid
from datetime import datetime

class Review():
    """"""
    def __init__(self, text, rating, place_id, user_id) -> None:
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
        self.created_at = datetime.now
        self.updated_at = datetime.now
        pass