
def knowsLeague():
    knowsLeague = {
        'state': 'knowsLeague',
        '`Do you have a favorite professional player?`': {
            '[yes]':{
                '`Oh, who is it?`': {
                    'error': {
                        '`See you later!`': 'end'
                    }
                }
            },
            '[{$FAVORITE_TEAM=#ONT(region)}]':{ #yeah, my favorite player is...
                '`They\'re doing really well right now.`': {
                    'error': {
                        '`See you later!`': 'end'
                    }
                }
            },
            '[{dont, know}, esports]':{ #"I don't know much about esports" - 'dont' doesn't work for some reason.
                '`Oh that\'s fine.`': {
                    'error': {
                        '`See you later!`': 'end'
                    }
                }
            },
            '[{dont, know}, {pro, player, players}]':{ #"I don't know much about esports" - 'dont' doesn't work for some reason.
                '`Do you have a favorite team?`': {
                    'error': {
                        '`See you later!`': 'end'
                    }
                }
            },
            'error': {
                '`I don\'t think I\'ve heard of them before. Can you tell me more about them?`': {
                    'error': {
                        '`Take care!`': 'end'
                    }
                }
            }
        }
    }
    return knowsLeague