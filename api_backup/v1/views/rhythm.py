#!/usr/bin/python3
'''Rhythm View'''
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.rhythm import Rhythm
from os import getenv, environ


@app_views.route('/rhythm/<rhythm_id>', methods=['GET'], strict_slashes=False)
def all_rhythm(rhythm_id):
    '''retrieves Rhythm object'''
    rhythm = storage.get('Rhythm', rhythm_id)
    if not rhythm:
        abort(404)
    return jsonify(rhythm.to_dict()), 200
