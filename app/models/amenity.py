from app.models.basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self) -> None:
        super().__init__() #does ID
        self.name = "???"
        #some additional data?