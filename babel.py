def babel():
    babel_transition = {
        'state': 'babel',
        '#GATE`What specific scenes from the movie regarding communication between the characters stood out to you?`': {
            'score': '1',
            'state': 'babelScenes',
            '[{chieko}]': {
                '`Sorry, could you repeat what scenes Chieko was in that stood out to you? `': 'babelScenes'
            },
            '[chieko, {ostracization, ostracized, ostracize, alone, removed, couldnt, communicate, communicating}]': {
                'state':'club',
                '`I agree. It must\'ve been difficult for Chieko. She can read body language, but she has to respond differently from how people are used to. Was there anything else in the movie that stood out to you?`': 'babelScenes'
            },
            '[chieko, {club, guy}]': 'club',
            '[{amelia, debbie, mike}, {mexico, desert}]': {
                '`That was an interesting scene too. What stood out to me was when the police didn\'t trust what Amelia was saying, and that their immediate reaction was to arrest her.`': 'babel'
            },
            '[{richard, susan}, {shot, wounded, hurt, bullet, bleeding}]': {
                '`Yeah, that was an interesting scene. Another scene that stood out to me was communicating through cultural differences, like when the older lady asked Susan to smoke, and Richard didn\'t understand that it would help her.`': 'babelScenes'
            },
            '[doctor, morocco]': {
                '`I agree. What stood out to me in that scene was when the tour guide was translating the doctor. I don\'t know the exact translation, but I\'m curious what the tour guide had to "filter out". Was there another scene you wanted to talk about?`': 'babelScenes'
            },
            '[{abdullah, yusef, ahmed}]': {
                '`Yeah, that scene was interesting to me, because even though the task of killing the jackals was clearly communicated to Yusef and Ahmed, what wasn\'t clearly communicated was the responsibility that had in holding a gun.`': 'babel'
            },
            '[{santiago, spanish}]': {
                '`I also find it was interesting that Santiago is often switching between English and Spanish. Any other scenes that stand out?`': 'babelScenes'
            },
            '[border]': {
                '`You\'re right. I think it\'s also normal that border control speaks in English, but are able to pick up a few phrases in Spanish and use that in their job. I don\'t speak Spanish, but I wonder what it feels like for those that do speak Spanish. Anything else that sticks out to you?`': 'babelScenes'
            },
            '[{lol, league}]': 'choseLeague',
            '[{no, none, nothing, not}]': {
                '`All good.`': 'babel'
            },
            'error': {
                '`Yeah, that was interesting.`': 'babel'
            }
        },
        '#GATE `Why do you think the title of the movie is "Babel?"`': {
            'score': '1',
            '[{tower}]': {
                '`Yeah, I also think it\'s related to the story of the Tower of Babel. It\'s pretty interesting looking at the parallels between the story and the movie.`': 'babel'
            },
            'error': {
                '`That\'s interesting. It\'s definitely related to the story of the Tower of Babel, are you familiar with it?`': {
                    '[#AgreementChecker]': {
                        '#IF(#POSITIVE_AGREEMENT)': {
                            '`Yeah, I think it\'s pretty interesting looking at the parallels between that story and the movie.`': 'babel'
                        },
                        '#IF(#NEGATIVE_AGREEMENT) `I\'ll give a quick summary. Long ago, a group of humans all speaking the same language wanted to build a tower with it\'s top in the sky. The ancient Levantine deity Yahweh struck down the tower and scattered the people\'s speech, which is why we all speak different languages today.`': {
                            'error': {
                                '`Yeah, I think it\'s pretty interesting looking at the parallels between that story and the movie.`': 'babel'
                            }
                        }
                    }
                }
            }
        },
        '`Would you like to talk about League of Legends now?`': {
            'score': '0.5',
            'error': 'choseLeague'
        }
    }

    return babel_transition