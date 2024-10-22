from uuid import UUID
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()


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
    # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        #amenity_id = UUID(str(amenity_id))
        return self.amenity_repo.get(amenity_id)

    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get_by_attribute("name", amenity_name)

    def get_all_amenities(self):
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity is None:
            return None
        #for key, value in amenity_data.items():
            #if hasattr(amenity, key):
                #setattr(amenity, key, value)
        amenity.update(amenity_data)
        return amenity

    ###
    ###PLACE
    ###

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.amenity_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place is None:
            return None
    
        if 'owner_id' in place_data:
            owner = self.get_user(place_data['owner_id'])
            if owner is None:
                raise ValueError('Invalid owner_id')
            
        if 'amenities' in place_data:
            for amenity_id in place_data['amenities']:
                if self.amenity_repo.get(amenity_id) is None:
                    raise ValueError(f'Invalid amenity_id: {amenity_id}')
                
        place.update(place_data)
        return place
    

    ###
    ###REVIEW
    ###

    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        return new_review
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