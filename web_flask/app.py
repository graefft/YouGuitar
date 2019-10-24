#!/usr/bin/python3
'''Front page'''
from flask import Flask, render_template, url_for
from web_flask.scale import Scales
from web_flask.chord import Chords

app = Flask(__name__, static_url_path='/static')

Scales = Scales()
Chords = Chords()

scales = [
    { 'name': 'Scale 1', 'id': '1' },
    { 'name': 'Scale 2', 'id': '2' },
    { 'name': 'Scale 3', 'id': '3' },
    { 'name': 'Scale 4', 'id': '4' },
    { 'name': 'Scale 5', 'id': '5' },
    { 'name': 'Scale 6', 'id': '6' },
    { 'name': 'Scale 7', 'id': '7' },
    { 'name': 'Scale 8', 'id': '8' },
    { 'name': 'Scale 9', 'id': '9' },
    { 'name': 'Scale 10', 'id': '10' }
 ]

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
@app.route('/scale', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    '''list lessons'''
    # lesson = storage.all(Lesson)
    return render_template('index.html',
                           scales=scales,
                           chords=chords,
                           rhythms=rhythms)

@app.route('/scales', strict_slashes=False)
def all_scales():
    return render_template('scales.html',
                            scales=scales)

@app.route('/scales/<scale_id>', strict_slashes=False)
def lesson(scale_id):
    return render_template('scale.html',
                           scales = Scales,
                           title='Scales', scale_id=scale_id)


@app.route('/chords', strict_slashes=False)
def all_chords():
    return render_template('chords.html',
                            chords=chords)

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
