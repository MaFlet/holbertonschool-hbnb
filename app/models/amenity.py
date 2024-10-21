import uuid

class Amenity():
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        pass