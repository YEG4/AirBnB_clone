import uuid
from datetime import datetime
from models import storage

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
           for key,value in kwargs.items():
               if key != "__class__":
                   if key == "created_at" or key == "updated_at":
                        setattr(self,key,datetime.fromisoformat(value))
                   else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        mydict = dict(self.__dict__)
        mydict['__class__'] = type(self).__name__
        return mydict

