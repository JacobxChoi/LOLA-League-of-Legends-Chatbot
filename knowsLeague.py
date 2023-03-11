
def knowsLeague():
    favoriteTeam = {
        'state': 'favPlayer',
        '`Who\'s your favorite professional player?`': {
            '[{#ONT(leagues)}]':{ #$FAV_PLAYER
                'state':'playerCondition',
                '`What do you think about how they\'ve been doing lately?`': {
                   '[{good, well, great, decent, nice, okay}]': {
                        '`That\'s valid, but I think jojopyun is in his prime right now.`':'end'
                    },
                    '[{hasnt, not, bad}]':{
                        '`I agree. (fav player) was much better before`': 'end'
                    },
                    'error':{
                        '`I\'m sorry, I didn\'t quite get that.`':'playerCondition' #error condition not handled
                    }
                }
            },
            'error':'favRegion' #if user doesn't have favorite player, go to favorite region
        }
    }
    favoriteRegion = {
        'state':'favRegion',
        '`What\'s your favorite region to watch?`':{
            '[favorite region]':{
                '`What are your thoughts on that particular tournament?`':'end' #leads to open ended response
            },
            'error':'end'
        }
    }
    return favoriteTeam, favoriteRegion