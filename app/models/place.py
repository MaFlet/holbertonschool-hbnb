from app.models.basemodel import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner) -> None:
        super.__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities <<<<-----------
        #Database of common amenities that can be referenced from and
        # then pulled into a place
        #For more specific amenities, have a system in place to add custom amenities???
        #Interface that allows one to add custom amenities. Still using the same amenity.
        pass

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

