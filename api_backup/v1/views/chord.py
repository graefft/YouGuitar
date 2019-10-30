#!/usr/bin/python3
'''Chord View'''
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.chord import Chord
from os import getenv, environ


@app_views.route('/chord/<chord_id>', methods=['GET'], strict_slashes=False)
def all_chord(chord_id):
    '''retrieves Chord object'''
    chord = storage.get('Chord', chord_id)
    if not chord:
        abort(404)
    return jsonify(chord.to_dict()), 200
