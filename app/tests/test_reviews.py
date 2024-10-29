import unittest
from uuid import uuid4
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.services.facade import HBnBFacade

class TestHBnBFacadeReview(unittest.TestCase):
    def setUp(self):
        self.facade = HBnBFacade()
        self.user_id = str(uuid4())
        self.place_id = str(uuid4())
        self.amenity_id = str(uuid4())
        
        # Create a user
        self.facade.create_user({'id': self.user_id, 'email': 'test@example.com', 'name': 'Test User'})
        
        # Create an amenity
        self.facade.create_amenity({'id': self.amenity_id, 'name': 'WiFi'})
        
        # Create a place
        self.facade.create_place({
            'id': self.place_id,
            'name': 'Test Place',
            'owner_id': self.user_id,
            'amenities': [self.amenity_id]
        })

    def test_create_review(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': 5,
            'comment': 'Great place!'
        }
        review = self.facade.create_review(review_data)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great place!')

    def test_create_review_invalid_user(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': str(uuid4()),  # Invalid user ID
            'place_id': self.place_id,
            'rating': 5,
            'comment': 'Great place!'
        }
        with self.assertRaises(ValueError) as context:
            self.facade.create_review(review_data)
        self.assertEqual(str(context.exception), f"user_id did not exist: {review_data['user_id']}")

    def test_create_review_invalid_place(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': str(uuid4()),  # Invalid place ID
            'rating': 5,
            'comment': 'Great place!'
        }
        with self.assertRaises(ValueError) as context:
            self.facade.create_review(review_data)
        self.assertEqual(str(context.exception), f"place_id did not exist: {review_data['place_id']}")

    def test_create_review_invalid_rating(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': 6,  # Invalid rating
            'comment': 'Great place!'
        }
        with self.assertRaises(ValueError) as context:
            self.facade.create_review(review_data)
        self.assertEqual(str(context.exception), "Rating must be an integet")

    def test_get_review(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': 5,
            'comment': 'Great place!'
        }
        review = self.facade.create_review(review_data)
        fetched_review = self.facade.get_review(review.id)
        self.assertEqual(fetched_review.id, review.id)

    def test_update_review(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': 5,
            'comment': 'Great place!'
        }
        review = self.facade.create_review(review_data)
        updated_data = {'rating': 4, 'comment': 'Good place!'}
        updated_review = self.facade.update_review(review.id, updated_data)
        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.comment, 'Good place!')

    def test_delete_review(self):
        review_data = {
            'id': str(uuid4()),
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': 5,
            'comment': 'Great place!'
        }
        review = self.facade.create_review(review_data)
        self.facade.delete_review(review.id)
        with self.assertRaises(ValueError) as context:
            self.facade.get_review(review.id)
        self.assertEqual(str(context.exception), f"Review with ID {review.id} not found")

if __name__ == "__main__":
    unittest.main()