from user import User
from app.models.place import Place


class BaseModel:
    """"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.first_name

        pass


class User(BaseModel):
    """"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__(first_name, last_name, email, is_admin)


def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")
test_user_creation()
