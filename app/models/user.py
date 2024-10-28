import uuid
from datetime import datetime
import re

class User():
    def __init__(self, first_name, last_name, email, is_admin=False) -> None:
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now
        self.updated_at = datetime.now
        self.places = []
        pass

    @property
    def first_name(self):
        """"""
        return self._first_name

    @first_name.setter
    def first_name(self, val):
        """"""
        if isinstance(val, str):
            self._first_name = val
        else:
            raise ValueError(
                "First name must be a valid string object"
            )
        
    @property
    def last_name(self):
        """"""
        return self._last_name

    @last_name.setter
    def last_name(self, val):
        """"""
        if isinstance(val, str):
            self._last_name = val
        else:
            raise ValueError(
                "First name must be a valid string object"
            )

    @property
    def email(self):
        """"""
        return self._email

    @email.setter
    def email(self, val):
        """"""
        if isinstance(val, str) and re.match(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', val):
            self._email = val
        else:
            raise ValueError("Invalid email address entered.")
    @property
    def is_admin(self):
        """"""
        return self._is_admin

    @is_admin.setter
    def is_admin(self, val):
        """"""
        if isinstance(val, bool):
            self._is_admin = val
        else:
            raise ValueError("is_admin must be a bool.")

    def add_place(self, place):
        """"""
        # Possibly necessary to do checks to see if place is a valid object
    
    def add_review(self, review):
        """"""
        # Again, validate review

    #def to_JSON(self):
    # Yeah... I figured this out pretty late
    # Anyway, up to the team whether or not we wanna do it here or in the API