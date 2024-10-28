import pytest
from datetime import datetime
from app.models.review import Review  

# Mock classes for Place and User
class MockPlace:
    def __init__(self, id):
        self.id = id

class MockUser :
    def __init__(self, id):
        self.id = id

def test_review_creation():
    place = MockPlace(id="place_1")
    user = MockUser (id="user_1")
    review = Review(text="Great place!", rating=5, place=place, user=user)

    assert review.text == "Great place!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    assert isinstance(review.created_at, datetime)
    assert isinstance(review.updated_at, datetime)

def test_review_text_validation():
    place = MockPlace(id="place_1")
    user = MockUser (id="user_1")

    # Valid text
    review = Review(text="Nice!", rating=5, place=place, user=user)
    assert review.text == "Nice!"

    # Invalid text (not a string)
    with pytest.raises(TypeError):
        review.text = 123

    # Invalid text (length too long)
    with pytest.raises(ValueError):
        review.text = "A" * 1001

    # Invalid text (length too short)
    with pytest.raises(ValueError):
        review.text = ""

def test_review_rating_validation():
    place = MockPlace(id="place_1")
    user = MockUser (id="user_1")

    # Valid rating
    review = Review(text="Good!", rating=4, place=place, user=user)
    assert review.rating == 4

    # Invalid rating (not an integer)
    with pytest.raises(TypeError):
        review.rating = "five"

    # Invalid rating (out of range)
    with pytest.raises(ValueError):
        review.rating = 6

    with pytest.raises(ValueError):
        review.rating = 0

def test_review_place_validation():
    user = MockUser (id="user_1")

    # Valid place