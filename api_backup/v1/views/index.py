#!/usr/bin/python3
'''Import app_views and create /status route on app_views'''
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.chord import Chord
from models.lesson import Lesson
from models.rhythm import Rhythm
from models.scale import Scale
from models.tuning import Tuning


@app_views.route('/status', strict_slashes=False)
def status():
    '''returns JSON: "status": OK'''
    result = {'status': 'OK'}
    return jsonify(result), 200
