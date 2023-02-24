
def knowsLeague():
    knowsLeague = {
        'state': 'knowsLeague',
        '`Do you have a favorite professional player?`': {
            '[yes]':{
                'state':'whichFavoritePlayer',
                '`Who is this player?`': {
                    '[faker]':{
                        'state':'teamCondition',
                        '`What do you think about how they\'ve been doing lately?`':'end' #continue conversation
                    },
                    'error': {
                        '`I don\'t think I know this player`': 'whichFavoritePlayer'
                    }
                }
            },
            '[{not}, {particularly}]':{
                '`What about a favorite team?`':{
                    '[favorite team]':'teamCondition'
                }
            },
            '[dont know]': {
                '`I really like Faker. Do you know them? `':{
                    '[yes]':'end', #continue conversation
                    '[no]':{
                        '`They play on T1. Do you know T1?`':'end' #continue conversation
                    }
                }
            },
            'error': { #favorite professional player
                '`I don\'t think I\'ve heard of them before. Can you tell me more about them?`':'end' #handle this case
            }
        }
    }
    return knowsLeague