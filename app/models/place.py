import uuid
from datetime import datetime
from app.models.user import User

class Place():
    """ """
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.amenities = amenities or []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if not isinstance(value, str):
            raise TypeError("Title must be string")
        if not 0 < len(value.strip()) <= 100:
            raise ValueError("Title length must be between 1 - 100 characters")
        self._title = value.strip()

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be string")
        if not 0 < len(value.strip()) <= 1000:
            raise ValueError("Description must be between 1 - 1000 characters in length")
        self._description = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            float_value = float(value)
            if float_value < 0:
                raise ValueError("We cannot accept negative value for price")
            self._price = float_value
        except (TypeError, ValueError) as e:
            if isinstance(e, TypeError) or str(e) != "Price cannot be negative":
                raise ValueError("The price must be a valid number") from e
            raise

    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Latitude must be a number")
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 to 90 degrees")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Longitude must be a number")
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 to 180 degrees")
        self._longitude = float(value)

    @property
    def owner_id(self):
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self, value):
        if not value:
            raise ValueError("Owner ID cannot be found")
        self._owner_id = str(value)
   
    def save(self):
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def add_review(self, review):
        self.reviews.append(review)


    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
