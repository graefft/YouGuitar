#!/usr/bin/python3
'''Scale View'''
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.scale import Scale
from os import getenv, environ


@app_views.route('/scale/<scale_id>', methods=['GET'],
                 strict_slashes=False)
def all_scale(scale_id):
    '''retrieves all objects of scale'''
    scale = storage.get('Scale', scale_id)
    if not scale:
        abort(404)
    return jsonify(scale.to_dict()), 200
