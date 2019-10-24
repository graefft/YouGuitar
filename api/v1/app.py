#!/usr/bin/python3
'''
Flask App to integrate YouGuitar HTML template
'''
from flask import Flask, jsonify
from flask import make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.url_map.strict_slashes = False

host = os.getenv('YG_API_HOST', '0.0.0.0')
port = os.getenv('YG_API_PORT', '5000')

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)

@app.errorhandler(400)
def handle_400(exception):
    handle_404(exception)


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
