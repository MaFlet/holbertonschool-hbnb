from app.models.basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name) -> None:
        super().__init__() #does ID
        self.name = name
        #some additional data?