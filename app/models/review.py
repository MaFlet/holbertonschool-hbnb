from app.models.basemodel import BaseModel

class Review(BaseModel):
    """"""
    def  __init__(self, text, rating, place, user) -> None:
        super().__init__()
        self.text = ""
        self.rating = 0
        self.place = None
        self.user = None
        pass
