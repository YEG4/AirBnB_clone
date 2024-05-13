import uuid
from datetime import datetime


class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        mydict = dict(self.__dict__)
        mydict['__class__'] = type(self).__name__
        return mydict


b = BaseModel()
print(b.to_dict())
