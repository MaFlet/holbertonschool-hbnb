import uuid
from datetime import datetime

class Review():
    """"""
    def __init__(self, text, rating, place, user):
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self,value):
        if not isinstance(value, str):
            raise TypeError("Text must be string")
        if not 0 < len(value.strip()) <= 1000:
            raise ValueError("Review length must be between 1 - 1000 characters only")
        self._text = value.strip()

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be a number")
        if not 1 <= value <=5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    @property
    def place(self):
        return self._place
    
    @place.setter
    def place(self, value):
        if value is None:
            raise ValueError("Place not found")
        if not hasattr(value, 'id'):
            raise TypeError("Invalid Place entity")
        self._place = value

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        if value is None:
            raise ValueError("User not found")
        if not hasattr(value, 'id'):
            raise TypeError("Invalid User Object")
        self._user = value
   
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
