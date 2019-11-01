#!/usr/bin/python3
'''Runs app and creates endpoints'''
from flask import Flask, render_template, url_for
from web_flask.scale import Scales
from web_flask.chord import Chords
from web_flask.rhythm import Rhythms

app = Flask(__name__, static_url_path='/static')

Scales = Scales()
Chords = Chords()
Rhythms = Rhythms()

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
    { 'title': 'Rhythm 1', 'id': '1' },
    { 'title': 'Rhythm 2', 'id': '2' },
    { 'title': 'Rhythm 3', 'id': '3' },
    { 'title': 'Rhythm 4', 'id': '4' },
    { 'title': 'Rhythm 5', 'id': '5' },
    { 'title': 'Rhythm 6', 'id': '6' },
    { 'title': 'Rhythm 7', 'id': '7' },
    { 'title': 'Rhythm 8', 'id': '8' },
    { 'title': 'Rhythm 9', 'id': '9' },
    { 'title': 'Rhythm 10', 'id': '10' }   ]

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/home', strict_slashes=False)
def home():
    '''lists all lessons'''
    return render_template('home.html',
                            scales=Scales,
                           chords=chord_by_lesson,
                           rhythms=rhythms)

@app.route('/lessons', strict_slashes=False)
def lessons():
    return render_template('lessons.html',
                            scales=Scales)


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

@app.route('/rhythms/<rhythm_id>', strict_slashes=False)
def rhythm(rhythm_id):
    return render_template('rhythm.html',
                            rhythms=Rhythms,
                            rhythm_id=rhythm_id,
                            title='Rhythms')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
