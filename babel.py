def babel():
    babel_transition = {
        'state':'babelTransition',
        '`What specific scenes from the movie regarding communication between the characters stood out to you?`':{
            'state':'babel',
            '[{chieko}]': {
                '`I\'m sorry. Could you repeat what scenes Chieko was in that stood out to you? `': 'babel'
            },
            '[chieko, {ostracization, ostracized, alone, removed, couldnt, communicate, communicating}]': {
                'state':'club',
                '`I agree. It must\'ve been difficult for Chieko. She can read body language, but she has to respond differently to what people are used to. Was there anything else in the movie that stood out to you?`': 'babel'
            },
            '[chieko, {club, guy}]':'club',
            '[{Amelia, Debbie, Mike}, {Mexico, desert}]': {
                '`That was an interesting scene too. What stood out to me was when the police didn\'t trust what Amelia was saying, and that their immediate reaction was to arrest her.`': 'babel'
            },
            '[{Richard, Susan}, {wounded, hurt, bullet, bleeding}]': {
                '`Yeah, that was an interesting scene.  Another scene that stood out to me was communicating through cultural differences, like when the older lady asked Susan to smoke, and Ricahrd didn\'t understand that it would help her`': 'babel'
            },
            '[doctor, Morocco]': {
                '`I agree. What stood out to me in that scene was when the tour guide was translating the doctor. I don\'t know the exact translation, but I\'m curious what the tour guide had to \'filter out\'. Do you have any thoughts?`': 'babel'
            },
            '[{Abdullah, Yusef, Ahmed}]': {
                '`Yeah, that scene was interesting to me, because even though the task of killing the jackals was clearly communicated to Yusef and Ahmed, what wasn\'t clearly communicated was the responsibility that had in holding a gun.`': 'babel'
            },
            'error': {
                '`Sorry, I don\'t actually remember that scene. Is there another scene that sticks out to you?`':'babel'
            }
        }
    }

    return babel_transition