import uuid
from datetime import datetime

"""Da basemodel"""

class BaseModel():
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = str(0)
        self.updated_at = str(0)

    def save(self):
        self.updated_at = datetime.now()
        pass

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()