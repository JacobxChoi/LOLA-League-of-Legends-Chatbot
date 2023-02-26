def doesntKnowLeague():
    doesntKnowLeague = {
        'state':'doesntKnowLeague',
        '`That\'s fine. Do you play League of Legends?.`': {
            '[yes]':{
                'state':'familiarity',
                '`Who\'s your favorite champion?`':{
                    '[favorite champion]':{
                        '`nice!`':'end'
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