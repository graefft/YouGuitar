#!/usr/bin/python3
'''Storage Class'''
import os
from models.base_model import BaseModel, Base
from models.lesson import Lesson
from sqlalchemy import create_engine
from sqlalcehmy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class Storage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('YG_MYSQL_USER')
        password = os.getenv('YG_MYSQL_PWD')
        host = os.getenv('YG_MYSQL_HOST')
        database = os.getenv('YG_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        
        def all(self, cls=None):
            class_list = ['Lesson', 'Tuning', 'Scale', 'Chord', 'Rhythm']
            all_dictionary = {}
            result_list = []
            if cls:
                result_list = self.__session.query(cls).all()
            else:
                for classes in class_list:
                    key = '{}.{}'.format(cls.__name__, classes.id)
                    all_dictionary[key] = classes
            return all_dictionary

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()

        def delete(self, obj=None):
            if obj:
                self.__session.delete(obj)

        def reload(self):
            Base.metadata.create_all(self.__engine)

            Session = scoped_session(sessionmaker(bind=self.__engine,
                                                  expire_on_commit=False))
            self.__session = Session()

        def close(self):
            self.__session.close()
