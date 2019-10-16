#!/usr/bin/python3
'''
Flask App to integrate YouGuitar HTML template
'''
from flask import Flask, jsonify
from flask import render_template
from models import storage
from models import BaseModel
from models import Lesson
import os

app = Flask(__name__)

host = os.getenv('YG_API_HOST', '0.0.0.0')
port = os.getenv('YG_API_PORT', '5000')


@app.route('/')
def home():
        return render_template('index.html')

@app.route('/lesson/<lesson_id>')
def lesson_by_id(lesson_id):
        lessons = storage.all(Lesson)
        selection = lessons.get('Lesson.{:}'.format(lesson_id))
        if selection is not None:
                return render_template('lesson.html', lesson=selection)
        else:
                return error(404)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
