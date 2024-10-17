import unittest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review

class TestUser(unittest.TestCase):
    def test_place_creation():
        """"""
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)

        review = Review(text="Great stay!", rating=5, place=place, user=owner)
        place.add_review(review)

        assert place.title == "Cozy Apartment"
        assert place.price == 100
        assert len(place.reviews) == 1
        assert place.reviews[0].text == "Great Stay!"
        print("Place creation and relationship test passed!")

if __name__ == "__main__":
    unittest.main()
