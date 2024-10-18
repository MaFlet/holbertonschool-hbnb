from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    ###
    ###USER
    ###
    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    ###
    ###AMENITY
    ###
    def create_amenity(self, amenity_data):
        """Validating created amenities"""
        if 'name' not in amenity_data or amenity_data['name'] == '' or all (char.isspace() for char in amenity_data['name']):
            raise ValueError("Amenity name is required")
        
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retreive amenity by ID"""
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError(f"Amenity with ID {amenity_id} not found")
        return amenity

    def get_all_amenities(self):
        """Retrieve list of amenities"""
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
    # Placeholder for logic to update an amenity
        pass

    ###
    ###PLACE
    ###
    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        pass

    ###
    ###REVIEW
    ###
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        pass

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        pass

    def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
        pass

    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        pass

    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        pass

    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        pass