import uuid

class Amenity():
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())
        self.name = name

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self