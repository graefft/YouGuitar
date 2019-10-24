#!/usr/bin/python3
'''Returns list of lessons'''
from flask import Flask, jsonify
from flask import abort, request
from api.v1.views import app_views
from models.lesson import Lesson


app = Flask(__name__)


@app._views.route('/lessons', methods=['GET'], strict_slashes=False)
def all_lessons():
    lessons = strorage.all(Lesson)
    lesson_list = []
    for lesson in lessons.values():
        lesson_list.append(lesson.to_dict())
    return jsonify(lesson_list), 200
