#!/usr/bin/python3
'''database for all scale information'''


def Scales():
    '''dictionary with all scale info'''
    scale_data = [
        {
            'id': '1',
            'type': 'pentatonic',
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
                            ''',
            'video': '<iframe width="560" height="315" src="https://www.youtube.com/embed/yzdCNSm_BU4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        },
        {
            'id': '2',
            'type': 'pentatonic',
            'title': 'E Pentatonic Scale',
            'body': '''e|---------------------------0-3--|<br/>
                       B|----------------------0-3-------|<br/>
                       G|-----------------0-2------------|<br/>
                       D|------------0-2-----------------|<br/>
                       A|-------0-2----------------------|<br/>
                       E|--0-3---------------------------|<br/>''',
            'description': '''This adds the second octave to our E Pentatonic scale. Play it left to right 
                              and backward then try with hammer-ons and pull-offs. When you are really 
                              comfortable playing it using downstrokes then try with alternate picking 
                              starting with a downstroke.''',
            'video': '<iframe width="560" height="315" src="https://www.youtube.com/embed/yzdCNSm_BU4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        },
        {
            'id': '3',
            'type': 'pentatonic',
            'title': 'Moveable Pentatonic Scale',
            'body': '''e|--------------------------------1-4--|<br/>
                       B|--------------------------1-4--------|<br/>
                       G|--------------------1-3--------------|<br/>
                       D|--------------1-3--------------------|<br/>
                       A|--------1-3--------------------------|<br/>
                       E|--1-4--------------------------------|<br/>''',
            'description': '''This version of the pentatonic scale allows us to play it in any key. 
                           Start by playing it at the first fret (key of Fm) but then try starting on a different 
                           fret (ex. 5th) and think of the numbers in the tab as finger numbers''',
            'video': '<iframe width="560" height="315" src="https://www.youtube.com/embed/rCNZy-pGyIo?start=25" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        },
        {
            'id': '4',
            'type': 'pentatonic',
            'title': 'Big E (minor) Pentatonic Scale',
            'body': '''e|-------------------------------------10-12--|<br/>
                       B|----------------------------8-10/12---------|<br/>
                       G|-----------------------7-9------------------|<br/>
                       D|----------------5-7/9-----------------------|<br/>
                       A|-----------5-7------------------------------|<br/>
                       E|--0-3-5/7-----------------------------------|<br/>''',
            'description': '''Now we have 3 octaves of E Pentatonic. Start with each octave (play first two strings, then 
                           from that 7th fret note and add next two strings, then that 9th fret note to end) then piece it 
                           all together slowly. Slide when indicated. Remember to practice it backward (you might change 
                           where the slides are on the way back, experiment with what feels best).''',
        },
        {
            'id': '5',
            'type': 'pentatonic',
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
            'type': 'diatonic',
            'title': 'C Major Scale',
            'body': '''e|----------------------|<br/>
                       B|-----------------0-1--|<br/>
                       G|------------0-2-------|<br/>
                       D|-----0-2-3------------|<br/>
                       A|--3-------------------|<br/>
                       E|----------------------|<br/>''',
            'description': '''The key of C Major is a good one to be comfortable with because it is the only major key 
                              without any sharps or flats. This is equivalent to playing only white keys on the piano and 
                              is the easiest way to play DO RE MI FA SOL LA TI DO on the guitar.'''
        },
        {
            'id': '7',
            'type': 'diatonic',
            'title': 'A Minor Scale',
            'body': '''e|---------------------|<br/>
                       B|---------------------|<br/>
                       G|----------------0-2--|<br/>
                       D|---------0-2-3-------|<br/>
                       A|--0-2-3--------------|<br/>
                       E|---------------------|<br/>''',
            'description': '''A minor is the relative minor of C major, meaning that it is comprised of the same notes, 
                              but just starts on A rather than C when we play it as a scale. It is a relatively easy 
                              pattern on guitar and can easily be transformed into a moveable version by adding 1 to 
                              each number.'''
        },
        {
            'id': '8',
            'type': 'diatonic',
            'title': 'E Phrygian Scale',
            'body': '''e|-----------------------------------0-1-3--|<br/>
                       B|----------------------------0-1-3---------|<br/>
                       G|-----------------------0-2----------------|<br/>
                       D|----------------0-2-3---------------------|<br/>
                       A|---------0-2-3----------------------------|<br/>
                       E|--0-1-3-----------------------------------|<br/>''',
            'description': '''E Phrygian is the mode name for when we take all the notes in C major (or A minor) 
                              but start on E. Here we are playing EFGABCDE notes in slightly more than 2 octaves. 
                              Many guitar sight-reading books start with learning these notes string-by-string.'''
        },
        {
            'id': '9',
            'type': 'diatonic',
            'title': 'Moveable Major Scale (one-octave)',
            'body': '''e|---------------------------|<br/>
                       B|---------------------------|<br/>
                       G|---------------------------|<br/>
                       D|---------------1-3-4-------|<br/>
                       A|--------1-2-4--------------|<br/>
                       E|---2-4---------------------|<br/>
                    ''',
            'description': '''This will allow us to play a major scale in any key. Start at 2nd fret (key of G flat) 
                              but then start on different frets and translating the tab to finger numbers. Remember 
                              that now the first middle finger note is the key you are in.'''
        },
        {
            'id': '10',
            'type': 'diatonic',
            'title': 'Moveable Major Scale (two-octaves)',
            'body': '''e|----------------------------------1-2---|<br/>
                       B|-----------------------------2-4--------|<br/>
                       G|----------------------1-3-4-------------|<br/>
                       D|---------------1-3-4--------------------|<br/>
                       A|--------1-2-4---------------------------|<br/>
                       E|---2-4----------------------------------|<br/>
                    ''',
            'description': '''We can now play two octaves of a major scale in any key. Watch out for the B string issue 
                              of no first-finger. Start on 2nd fret, play up and down and then repeat on ascending frets 
                              until you run out of room (or hand gets tired).'''
        }

    ]
    return scale_data
