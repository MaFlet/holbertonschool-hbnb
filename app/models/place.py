import uuid
from datetime import datetime

class Place():
    """ """
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longtitude = longitude
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
        if not 0 < len(value.strip() <= 1000):
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
                raise ValueError("The price must be a valid number")
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
        if not isinstance(value, str):
            raise TypeError("Owner ID must be a string")
        try:
            uuid.UUID(value.strip())
            self._owner_id = value.strip()
        except ValueError:
            raise ValueError("Owner IO must be in valid format")
        
    @property
    def created_at(self):
        return self._created_at
        
    @property
    def updated_at(self):
        return self.updated_at
    
    @updated_at.setter
    def updated_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Updated should be correct datetime object")
        self._updated_at = value

    @property
    def reviews(self):
        return self._reviews
    
    @reviews.setter
    def reviews(self, value):
        if not isinstance(value, list):
            raise TypeError("Reviews must be a list")
        self._reviews = value

    @property
    def amenities(self):
        return self._amenities
    
    @amenities.setter
    def amenities(self, value):
        if not isinstance(value, list):
            raise TypeError("Amenities must be a list")
        self._amenities = value

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.updated_at = datetime.now()
    
    
