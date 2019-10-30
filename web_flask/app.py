#!/usr/bin/python3
'''Front page'''
from flask import Flask, render_template, url_for
from web_flask.scale import Scales
from web_flask.chord import Chords

app = Flask(__name__, static_url_path='/static')

Scales = Scales()
Chords = Chords()

chords = [
    { 'name': 'Chord 1', 'id': '1' },
    { 'name': 'Chord 2', 'id': '2' },
    { 'name': 'Chord 3', 'id': '3' },
    { 'name': 'Chord 4', 'id': '4' },
    { 'name': 'Chord 5', 'id': '5' },
    { 'name': 'Chord 6', 'id': '6' },
    { 'name': 'Chord 7', 'id': '7' },
    { 'name': 'Chord 8', 'id': '8' },
    { 'name': 'Chord 9', 'id': '9' },
    { 'name': 'Chord 10', 'id': '10' },
    { 'name': 'Chord 11', 'id': '11' },
    { 'name': 'Chord 12', 'id': '12' }
    ]

chord_by_lesson = [
    { 'title': 'Power Chords (2-note)', 'id': '1' },
    { 'title': 'Power Chords (3-note)', 'id': '2' },
    { 'title': 'Chords in Key of G', 'id': '3' },
    { 'title': 'Chords in Key of A', 'id': '4' },
    { 'title': 'Chords in Key of C', 'id': '5' },
    { 'title': 'Chords in Key of F', 'id': '6' },
    { 'title': 'Chords in Key of Dm', 'id': '7' }
    ]


rhythms = [
    { 'name': 'Rhythm 1', 'id': '1' },
    { 'name': 'Rhythm 2', 'id': '2' },
    { 'name': 'Rhythm 3', 'id': '3' },
    { 'name': 'Rhythm 4', 'id': '4' },
    { 'name': 'Rhythm 5', 'id': '5' },
    { 'name': 'Rhythm 6', 'id': '6' },
    { 'name': 'Rhythm 7', 'id': '7' }
    ]

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/home', strict_slashes=False)
def home():
    '''list lessons'''
    return render_template('home.html',
                           scales=Scales,
                           chords=chord_by_lesson,
                           rhythms=rhythms)

@app.route('/scale', strict_slashes=False)
@app.route('/scales', strict_slashes=False)
def all_scales():
    return render_template('scales.html',
                            scales=Scales)

@app.route('/scales/<scale_id>', strict_slashes=False)
def lesson(scale_id):
    return render_template('scale.html',
                           scales=Scales,
                           title='Scales', scale_id=scale_id)


@app.route('/chords', strict_slashes=False)
def all_chords():
    return render_template('chords.html',
                            chords=chord_by_lesson)

@app.route('/chords/<chord_id>', strict_slashes=False)
def chord(chord_id):
    return render_template('chord.html',
                           chords=Chords,
                           title='Chords', chord_id=chord_id)

@app.route('/rhythms', strict_slashes=False)
def all_rhythms():
    return render_template('rhythms.html',
                            title='Rhythms',
                            rhythms=rhythms)

@app.route('/01')
def lesson_01(lesson_id='01'):
    return render_template('lesson.html',
                           title='Lesson')

#@app.teardown_appcontext
#def clean_up(self):
#    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
