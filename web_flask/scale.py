#!/usr/bin/python3

def Scales():
    scale_data = [
        {
            'id': '1',
            'type': 'scale',
            'title': 'E Pentatonic Scale',
            'body': '''e|------------------------|<br/>
                       B|------------------------|<br/>
                       G|------------------------|<br/>
                       D|---------------0--2-----|<br/>
                       A|---------0--2-----------|<br/>
                       E|---0--3-----------------|<br/>
                    ''',
            'description': '''The prefix "penta" means <em>five</em>. This is a 5 note scale 
                            that is the foundation of most rock and pop improvisation. 
                            Practice it slowly and play it left to right as well as right to left.
                            '''
        },
        {
            'id': '2',
            'type': 'scale',
            'title': 'E Pentatonic Scale',
            'body': '''|---------------------------0-3--|<br/>
                       |----------------------0-3-------|<br/>
                       |-----------------0-2------------|<br/>
                       |------------0-2-----------------|<br/>
                       |-------0-2----------------------|<br/>
                       |--0-3---------------------------|<br/>''',
            'description': '''This adds the second octave to our E Pentatonic scale'''
        },
        {
            'id': '3',
            'type': 'scale',
            'title': 'Moveable Pentatonic Scale',
            'body': '''|--------------------------------1-4--|<br/>
                       |--------------------------1-4--------|<br/>
                       |--------------------1-3--------------|<br/>
                       |--------------1-3--------------------|<br/>
                       |--------1-3--------------------------|<br/>
                       |--1-4--------------------------------|<br/>''',
            'description': '''This version of the pentatonic scale allows us to play it in any key. 
                           Start by playing it at the first fret (key of Fm) but then try starting on a different 
                           fret (ex. 5th) and think of the numbers in the tab as finger numbers'''
        },
        {
            'id': '4',
            'type': 'scale',
            'title': 'Big E (minor) Pentatonic Scale',
            'body': '''|-------------------------------------10-12--|<br/>
                       |----------------------------8-10/12---------|<br/>
                       |-----------------------7-9------------------|<br/>
                       |----------------5-7/9-----------------------|<br/>
                       |-----------5-7------------------------------|<br/>
                       |--0-3-5/7-----------------------------------|<br/>''',
            'description': '''Now we have 3 octaves of E Pentatonic. Start with each octave (play first two strings, then 
                           from that 7th fret note and add next two strings, then that 9th fret note to end) then piece it 
                           all together slowly. Slide when indicated. Remember to practice it backward (you might change 
                           where the slides are on the way back, experiment with what feels best).''',
        },
        {
            'id': '5',
            'type': 'scale',
            'title': 'Big A (minor) Pentatonic Scale',
            'body': '''e|---------------------------------8-10/12--|<br/>
                       B|---------------------------8-10-----------|<br/>
                       G|---------------------5-7/9----------------|<br/>
                       D|----------------5-7-----------------------|<br/>
                       A|---------3-5/7----------------------------|<br/>
                       E|--0-3-5-----------------------------------|<br/>''',
            'description': '''The notes in this scale are A C D E G. In this case we start on E so just remember 
                              that the A root note is 5th fret on E string, 7th fret D string, and 10th fret B string.'''
        },
        {
            'id': '6',
            'type': 'scale',
            'title': 'C Major Scale',
            'body': '''|----------------------|<br/>
                       |-----------------0-1--|<br/>
                       |------------0-2-------|<br/>
                       |-----0-2-3------------|<br/>
                       |--3-------------------|<br/>
                       |----------------------|<br/>''',
            'description': '''The key of C Major is a good one to be comfortable with because it is the only major key 
                              without any sharps or flats. This is equivalent to playing only white keys on the piano and 
                              is the easiest way to play DO RE MI FA SOL LA TI DO on the guitar.'''
        },
        {
            'id': '7',
            'type': 'scale',
            'title': 'A Minor Scale',
            'body': '''|---------------------|<br/>
                       |---------------------|<br/>
                       |----------------0-2--|<br/>
                       |---------0-2-3-------|<br/>
                       |--0-2-3--------------|<br/>
                       |---------------------|<br/>''',
            'description': '''A minor is the relative minor of C major, meaning that it is comprised of the same notes, 
                              but just starts on A rather than C when we play it as a scale. It is a relatively easy 
                              pattern on guitar and can easily be transformed into a moveable version by adding 1 to 
                              each number.'''
        },
        {
            'id': '8',
            'type': 'scale',
            'title': 'E Phrygian Scale',
            'body': '''|-----------------------------------0-1-3--|<br/>
                       |----------------------------0-1-3---------|<br/>
                       |-----------------------0-2----------------|<br/>
                       |----------------0-2-3---------------------|<br/>
                       |---------0-2-3----------------------------|<br/>
                       |--0-1-3-----------------------------------|<br/>''',
            'description': '''E Phrygian is the mode name for when we take all the notes in C major (or A minor) 
                              but start on E. Here we are playing EFGABCDE notes in slightly more than 2 octaves. 
                              Many guitar sight-reading books start with learning these notes string-by-string.'''
        },
        {
            'id': '9',
            'type': 'scale',
            'title': 'Moveable Major Scale (one-octave)',
            'body': '''|---------------------------|<br/>
                       |---------------------------|<br/>
                       |---------------------------|<br/>
                       |---------------1-3-4-------|<br/>
                       |--------1-2-4--------------|<br/>
                       |---2-4---------------------|<br/>
                    ''',
            'description': '''This will allow us to play a major scale in any key. Start at 2nd fret (key of G flat) 
                              but then start on different frets and translating the tab to finger numbers. Remember 
                              that now the first middle finger note is the key you are in.'''
        },
        {
            'id': '10',
            'type': 'scale',
            'title': 'Moveable Major Scale (two-octaves)',
            'body': '''|----------------------------------1-2---|<br/>
                       |-----------------------------2-4--------|<br/>
                       |----------------------1-3-4-------------|<br/>
                       |---------------1-3-4--------------------|<br/>
                       |--------1-2-4---------------------------|<br/>
                       |---2-4----------------------------------|<br/>
                    ''',
            'description': '''We can now play two octaves of a major scale in any key. Watch out for the B string issue 
                              of no first-finger. Start on 2nd fret, play up and down and then repeat on ascending frets 
                              until you run out of room (or hand gets tired).'''
        }

    ]
    return scale_data
