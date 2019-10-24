'''creates instance of FileStorage'''
from models.base_model import BaseModel
from models.engine.storage import Storage
from models.lesson import Lesson

storage = Storage()
storage.reload()
