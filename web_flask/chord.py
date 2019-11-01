#!/usr/bin/python3

def Chords():
    chord_data = [
        {
            'id': '1',
            'lesson_id': '1',
            'type': 'Power Chords',
            'title': 'E5 Power Chord',
            'image': '../static/images/E5_chord-2.png',
            'description': '''Chords with a 5 suffix are often referred to as <em>power chords</em>. 
                              They are two-note chords that can sound powerful for their size. They 
                              are comprised of the root note and the 5th note in the diatonic scale. 
                           ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/OVDcMk6S-p8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id':'2',
            'lesson_id': '1',
            'type': 'Power Chords',
            'title': 'A5 Power Chord',
            'image': '../static/images/A5_chord-2.png',
            'description': '''Chords with a 5 suffix are often referred to as <em>power chords</em>. 
                              They are two-note chords that can sound powerful for their size. They 
                              are comprised of the root note and the 5th note in the diatonic scale. 
                           ''',
            },
        {
            'id': '3',
            'lesson_id': '1',
            'type': 'Power Chords',
            'title': 'D5 Power Chord',
            'image': '../static/images/D5_chord-2.png',
            'description': '''Chords with a 5 suffix are often referred to as <em>power chords</em>. 
                              They are two-note chords that can sound powerful for their size. They 
                              are comprised of the root note and the 5th note in the diatonic scale. 
                           ''',
        },
        {
            'id': '4',
            'lesson_id': '2',
            'type': 'Power Chords (3-note)',
            'title': 'E5 Power Chord (3 note)',
            'image': '../static/images/E5_chord-3.png',
            'description': '''These 3-note versions of the E5 A5 and D5 add a third note. This is an octave 
                           higher than the root note so the chord is still comprised of the root and 5th''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/ik9TGv4YNX8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id': '5',
            'lesson_id': '2',
            'type': 'Power Chords (3-note)',
            'title': 'A5 Power Chord (3 note)',
            'image': '../static/images/A5_chord-3.png',
            'description': '''These 3-note versions of the E5 A5 and D5 add a third note. This is an octave 
                           higher than the root note so the chord is still comprised of the root and 5th''',
 
        },
        {
            'id': '6',
            'lesson_id': '2',
            'type': 'Power Chords (3-note)',
            'title': 'D5 Power Chord (3 note)',
            'image': '../static/images/D5_chord-3.png',
            'description': '''These 3-note versions of the E5 A5 and D5 add a third note. This is an octave 
                           higher than the root note so the chord is still comprised of the root and 5th''',
 
        },
        {
            'id': '7',
            'lesson_id': '3',
            'type': 'Chords in Key of G',
            'title': 'Em Chord',
            'image': '../static/images/Em_chord.png',
            'description': '''Use the first and second finger to play the Em chord. Keep your first finger 
                              in the same spot when switching to the G chord. Go back and forth a lot. We 
                              use these chords together all the time.
                            ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/_NsdSzYb-N0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id': '8',
            'lesson_id': '3',
            'type': 'Chords in Key of G',
            'title': 'G Chord',
            'image': '../static/images/G_chord.png',
            'description': '''Use the first and second finger to play the Em chord. Keep your first finger 
                              in the same spot when switching to the G chord. Go back and forth a lot. We 
                              use these chords together all the time.
                            '''
        
        },
        {
            'id': '9',
            'lesson_id': '4',
            'type': 'Chords in Key of A',
            'title': 'A Chord',
            'image': '../static/images/A_chord.png',
            'description': '''The standard way to play A is with the first 3 fingers squeezed closely 
                              together. Try 2nd, 3rd, and 4th fingers if you have larger hands. A lot of 
                              times we will use a 1st finger flat across these three dots but for now try 
                              to make it three fingers. The 2nd fret note on the high E string for the D 
                              chord can be troublesome, don't worry if you can't get it to sound at first. 
                              Make sure that finger stays behind the fret and that 3rd finger doesn't 
                              block it from ringing. The E chord should be somewhat more comfortable, just 
                              make sure to keep the 1st finger close to the fret on the G string note.
                            ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/pBacbX9yefA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id': '10',
            'lesson_id': '4',
            'type': 'Chords in Key of A',
            'title': 'D Chord',
            'image': '../static/images/D_chord.png',
            'description': '''The standard way to play A is with the first 3 fingers squeezed closely 
                              together. Try 2nd, 3rd, and 4th fingers if you have larger hands. A lot of 
                              times we will use a 1st finger flat across these three dots but for now try 
                              to make it three fingers. The 2nd fret note on the high E string for the D 
                              chord can be troublesome, don't worry if you can't get it to sound at first. 
                              Make sure that finger stays behind the fret and that 3rd finger doesn't 
                              block it from ringing. The E chord should be somewhat more comfortable, just 
                              make sure to keep the 1st finger close to the fret on the G string note.
                            ''',
        },
        {
            'id': '11',
            'lesson_id': '4',
            'type': 'Chords in Key of A',
            'title': 'E Chord',
            'image': '../static/images/E_chord.png',
            'description': '''The standard way to play A is with the first 3 fingers squeezed closely 
                              together. Try 2nd, 3rd, and 4th fingers if you have larger hands. A lot of 
                              times we will use a 1st finger flat across these three dots but for now try 
                              to make it three fingers. The 2nd fret note on the high E string for the D 
                              chord can be troublesome, don't worry if you can't get it to sound at first. 
                              Make sure that finger stays behind the fret and that 3rd finger doesn't 
                              block it from ringing. The E chord should be somewhat more comfortable, just 
                              make sure to keep the 1st finger close to the fret on the G string note.
                           ''',
        },
        {
            'id': '12',
            'lesson_id': '5',
            'type': 'Chords in Key of C',
            'title': 'C Chord',
            'image': '../static/images/C_chord.png',
            'description': '''The important thing to note here is that the 1st and 2nd fingers stay in the 
                              same spots between the C and Am chords. We will see these two chords together
                               all the time so try switching between them by only moving the 3rd finger. 
                              Recognizing these shortcuts will help tremendously with speeding up chord 
                              changes.
                            ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/DbcW1Fm6LsQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id': '13',
            'lesson_id': '5',
            'type': 'Chords in Key of C',
            'title': 'Am Chord',
            'image': '../static/images/Am_chord.png',
            'description': '''The important thing to note here is that the 1st and 2nd fingers stay in the 
                              same spots between the C and Am chords. We will see these two chords together
                               all the time so try switching between them by only moving the 3rd finger. 
                              Recognizing these shortcuts will help tremendously with speeding up chord 
                              changes.
                            '''
        },
        {
            'id': '14',
            'lesson_id': '6',
            'type': 'Chords in Key of F',
            'title': 'F Chord',
            'image': '../static/images/F_chord-3.png',
            'description': '''The F chord is annoying at first for any guitarist. Start with the 3-finger 
                              version which shouldn't be too difficult. To add the 1st finger flat across 
                              the high E string, try bringing the thumb way down on the back of the neck 
                              toward the floor. For the barre chord version, keep the left elbow down and 
                              bottom of hand outward from the guitar to allow the 1st finger to go straight 
                              across all the strings.
                           ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/pbyHseP4NLo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        },
        {
            'id': '15',
            'lesson_id': '6',
            'type': 'Chords in Key of F',
            'title': 'F Chord',
            'image': '../static/images/F_chord-4.png',
            'description': '''The F chord is annoying at first for any guitarist. Start with the 3-finger 
                              version which shouldn't be too difficult. To add the 1st finger flat across 
                              the high E string, try bringing the thumb way down on the back of the neck 
                              toward the floor. For the barre chord version, keep the left elbow down and 
                              bottom of hand outward from the guitar to allow the 1st finger to go straight 
                              across all the strings.
                           ''',
        },
        {
            'id': '16',
            'lesson_id': '6',
            'type': 'Chords in Key of F',
            'title': 'F Chord',
            'image': '../static/images/F_chord-6.png',
            'description': '''The F chord is annoying at first for any guitarist. Start with the 3-finger 
                              version which shouldn't be too difficult. To add the 1st finger flat across 
                              the high E string, try bringing the thumb way down on the back of the neck 
                              toward the floor. For the barre chord version, keep the left elbow down and 
                              bottom of hand outward from the guitar to allow the 1st finger to go straight 
                              across all the strings.
                           ''',
        },
        {
            'id': '17',
            'lesson_id': '7',
            'type': 'Chords in Key of Dm',
            'title': 'Dm Chord',
            'image': '../static/images/Dm_chord.png',
            'description': '''The D minor chord will pop up often, especially in songs in keys of Am, F, 
                              and C. Keep the fingers really curvy and experiment with where the thumb is 
                              placed. Make sure to keep the 1st finger really close to the fret on the 
                              high E string. If it is too hard to push down, consider lighter strings or 
                              adjusting the action on your guitar.
                           ''',
            'video': '''<iframe width="560" height="315" src="https://www.youtube.com/embed/Vq6dw9zG5PY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        }
    ]
    return chord_data
