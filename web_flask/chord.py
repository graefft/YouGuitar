#!/usr/bin/python3

def Chords():
    chord_data = [
        {
            'id': '1',
            'type': 'chord',
            'title': 'E Pentatonic Chord',
            'body': '''|---------------------------0-3--|<br/>
                       |----------------------0-3-------|<br/>
                       |-----------------0-2------------|<br/>
                       |------------0-2-----------------|<br/>
                       |-------0-2----------------------|<br/>
                       |--0-3---------------------------|<br/>'''
        },
        {
            'id':'2',
            'type': 'chord',
            'title': 'Moveable Pentatonic Chord',
            'body': '''|---------------------------1-4--|<br/>
                       |----------------------1-4-------|<br/>
                       |-----------------1-3------------|<br/>
                       |------------1-3-----------------|<br/>
                       |-------1-3----------------------|<br/>
                       |--1-4---------------------------|<br/>'''
        },
        {
            'id': '3',
            'type': 'chord',
            'title': 'Big E (minor) Pentatonic Chord',
            'body': '''|--------------------------------10-12--|<br/>
                       |------------------------8-10/12--------|<br/>
                       |--------------------7-9----------------|<br/>
                       |--------------5-7/9--------------------|<br/>
                       |----------5-7--------------------------|<br/>
                       |--0-3-5/7------------------------------|<br/>'''
        },
        {
            'id': '4',
            'type': 'chord',
            'title': 'Big A (minor) Pentatonic Chord',
            'body': '''|---------------------------------8-10/12--|<br/>
                       |---------------------------8-10-----------|<br/>
                       |---------------------5-7/9----------------|<br/>
                       |----------------5-7-----------------------|<br/>
                       |---------3-5/7----------------------------|<br/>
                       |--0-3-5-----------------------------------|<br/>'''
        },
        {
            'id': '5',
            'type': 'chord',
            'title': 'C Major Chord',
            'body': '''|----------------------|<br/>
                       |-----------------0-1--|<br/>
                       |------------0-2-------|<br/>
                       |-----0-2-3------------|<br/>
                       |--3-------------------|<br/>
                       |----------------------|<br/>'''
        },
        {
            'id': '6',
            'type': 'chord',
            'title': 'A Minor Chord',
            'body': '''|---------------------|<br/>
                       |---------------------|<br/>
                       |----------------0-2--|<br/>
                       |---------0-2-3-------|<br/>
                       |--0-2-3--------------|<br/>
                       |---------------------|<br/>'''
        },
        {
            'id': '7',
            'type': 'chord',
            'title': 'E Phrygian Chord',
            'body': '''|-----------------------------------0-1-3--|<br/>
                       |----------------------------0-1-3---------|<br/>
                       |-----------------------0-2----------------|<br/>
                       |----------------0-2-3---------------------|<br/>
                       |---------0-2-3----------------------------|<br/>
                       |--0-1-3-----------------------------------|<br/>'''
        }
    ]
    return chord_data
