#!/usr/bin/python3
'''
Lessons View
'''
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.lesson import Lesson
from os import getenv, environ


@app_views.route('/lesson', methods=['GET'], strict_slashes=False)
def all_lessons():
    '''Retrieve all lesson objects'''
    return jsonify([l.to_dict() for l in storage.all('Lesson').values()]), 200


@app_views.route('/lesson/<lesson_id>', methods=['GET'], strict_slashes=False)
def lesson_by_id(lesson_id=' '):
    '''Lesson by ID'''
    lesson = storage.get('Lesson', lesson_id)
    if not lesson:
        abort(404)
    output = lesson.to_dict()
    return jsonify(output), 200
