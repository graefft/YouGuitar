#!/usr/bin/python3
"""This module serializes and deserializes instances"""

import json
from models.base_model import BaseModel
from models.tuning import Tuning
from models.scale import Scale
from models.chord import Chord
from models.rhythm import Rhythm
from os import path


class FileStorage:
    """A class named FileStorage
    Attributes:
    attr1(__file_path): path to the JSON file
    attr2(__objects): dictionary for all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects dictionary to the JSON file"""
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as w:
            json.dump(dictionary, w)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dictionaryofdictionaries = {}
        classes = {
            'BaseModel': BaseModel,
            "Tuning": Tuning,
            'Scale': Scale,
	    'Chord': Chord,
            'Rhythm': Rhythm
	}
	try:
            with open(self.__file_path, "r") as r:
                dict_of_dict = json.load(r)
                for k, v in dict_of_dict.items():
                    if v["__class__"] in classes:
                        self.__objects[k] = classes[v["__class__"]](**v)
        except:
            pass

    def reset(self):
        """Resets objects dict to empty dictionary"""
        self.__objects = {}
