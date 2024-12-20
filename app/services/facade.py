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
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        str_id = str(user_id)
        return self.user_repo.get(str_id)
    
    def get_all_user(self):
        return list(self.user_repo.get_all())
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None
        
        self.user_repo.update(user_id, user_data)
        return self.get_user(user_id)
    
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
        owner_id = place_data.get('owner_id') # validate if owner exists
        if not owner_id:
            raise ValueError("Owner ID is required")
        
        owner = self.get_user(str(owner_id))
        if not owner:
            raise ValueError(f"Owner with ID {owner_id} not found")
        
        place = Place(**place_data) # to create place with validated owner
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return list(self.place_repo.get_all())

    def update_place(self, place_id, place_data, requesting_user_id):
        place = self.get_place(place_id)
        if not place:
            raise ValueError(f"Place with ID {place_id} not found")

        if str(place.owner.id) != str(requesting_user_id):
            raise ValueError("Only the owner can update this place")
        
        return self.place_repo.update(place_id, place_data)

    ###
    ###REVIEW
    ###

    def create_review(self, review_data):
        user_id = review_data.get('user_id') #validating if user exists
        if not self.get_user(user_id):
            raise ValueError(f"user_id did not exist: {user_id}")
        
        place_id = place_data.get('place_id')
        if not self.get_place(place_id):
            raise ValueError(f"place_id did not exist: {place_id}")
        
        rating = review_data.get('rating')
        if not isinstance(rating, int) or not 1<= rating <=5:
            raise ValueError("Rating must be an integet")
        
        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        return new_review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return list(self.review_repo.get_all())

    def get_reviews_by_place(self, place_id):
         return self.review_repo.get_by_attribute("place_id", place_id)

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review is None:
            raise ValueError(f"Review with ID {review_id} not found")
        
        if 'rating' in review_data:
            rating = review_data['rating']
            if not isinstance(rating, int) or not 1 <= rating <= 5:
                raise ValueError("Rating must be a number")
            
        return self.review_repo.update(review_id, review_data)
    
    def delete_review(self, review_id):
        if not review_id:
            raise ValueError("Review ID cannot be empty")
        
        review = self.get_review(review_id)
        if review is None:
            raise ValueError(f"Review with ID {review_id} not found")
        
        return self.review_repo.delete(review_id)
        