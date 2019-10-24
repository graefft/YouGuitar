#!/usr/bin/python3
from flask import Flask, jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    if request.method == 'GET':
        return jsonify({'status':'OK'}}