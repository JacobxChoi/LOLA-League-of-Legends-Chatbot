def doesntKnowLeague():
    doesntKnowLeague = {
        'state':'doesntKnowLeague',
        '`That\'s fine. Are you familiar with the game League of Legends?.`': {
            '[yes]':{
                'state':'familiarity',
                '`Do you have a general idea of what esports is?`':{
                    '[yes]':{
                        '`Have you ever heard of C9?`':'end' #continue conversation
                    },
                    '[no]':{
                        '`Esports is a competitive gaming league where teams play games like League of Legends and compete for prizes. Does that make sense?`': {
                            '[yes]':{
                                '`Awesome!`''end'
                            },
                            '[no]':{
                                '`What are you confused about?`':'end' #continue conversation
                            },
                            'error':'end'
                        }
                    },
                    'error':'end'
                }
            },
            '[no]':{
                '`League of Legends is an online 5 v 5 game, where players play \'champions\' that each have unique abilites. The objective of the game is to kill the enemy player\'s nexus. Does that make sense?`':{
                    '[yes]': 'familiarity',
                    '[no]':{
                        '`What are you confused about?`':'end' #continue conversation
                    },
                    'error':'end'
                }
            },
            'error':'doesntKnowLeague'
        }
    }
    return doesntKnowLeague