#!/usr/bin/python3
'''Lesson Class'''
import models
import os
from models.base_model import Base, BaseModel
from models.lesson import Lesson
from sqlalchemy import Column, Integer, String


class Lesson(BaseModel, Base):
    __tablename__ = 'lessons'
    lesson_id = Column(Integer, nullable=False)
    lesson_name = Column(String(128), nullable=False)
