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
