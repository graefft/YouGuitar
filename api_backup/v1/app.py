#!/usr/bin/python3
'''
Flask app to serve HTML pages
'''
from flask import Flask, jsonify, make_response, render_template
#from models import storage
import os
from werkzeug.exceptions import HTTPException, NotFound


app = Flask(__name__)
app.url_map.strict_slashes = False

host = os.getenv('YG_API_HOST', '0.0.0.0')
port = os.getenv('YG_API_HOST', 5000)

#@app.teardown_appcontext
#def teardown_db(exception):
#    '''close() current SQLAlchemy session'''
#    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    '''handles 404 errors'''
    error_code = exception.__str__().split()[0]
    description = exception.description
    message = {'ERROR': description}
    return make_response(jsonify(message), code)


@app.errorhandler(Exception)
def global_error_handler(err):
    '''global route to handle Error status codes'''
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.descripton = 'Not found'
        message = {'ERROR': err.description}
        code = err.code
    else:
        message = {'ERROR': err}
        code = 500
    return make_response(jsonify(message), code)

def setup_global_error():
    '''updates HTTPException with custom error function'''
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == '__main__':
    '''initialize error handling and start Flask'''
    setup_global_error()
    app.run(host=host, port=port)
