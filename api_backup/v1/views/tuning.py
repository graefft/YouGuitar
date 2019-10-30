#!/usr/bin/python3
'''Tuning View'''
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.tuning import Tuning
from os import getenv, environ


@app_views.route('/tuning/<tuning_id>', methods=['GET'], strict_slashes=False)
def all_tuning(tuning_id):
    '''retrieves Tuning object'''
    tuning = storage.get('Tuning', tuning_id)
    if not tuning:
        abort(404)
    return jsonify(tuning.to_dict()), 200
