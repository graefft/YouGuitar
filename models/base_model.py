#!/usr/bin/python3
'''creates BaseModel class'''
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4


Base = declarative_base()

class BaseModel:

    id = Column(String(10),
         nullable=False,
         primary_key=True)

    created_at = Column(DateTime,
                        default=datetime.utcnow())
    
    updated_at = Column(DateTime,
                        default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    datetimeObject = datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, datetimeObject)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''class name, id, and dictionary'''
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id,
                                     self.to_dict())

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = datetime.isoformat(new_dictionary['created_at'])
        new_dictionary['updated_at'] = datetime.isoformat(new_dicitonary['updated_at'])
        return new_dictionary
