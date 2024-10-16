import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, first_name, last_name, email, is_admin = False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class User(BaseModel):
    """"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__(first_name, last_name, email, is_admin)

if __name__ == "__main__":
    def test_user_creation():
        user =  BaseModel(first_name="John", last_name="Doe", email="john.doe@example.com")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False  # Default value
        print("User creation test passed!")
