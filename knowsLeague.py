
def knowsLeague():
    favoriteTeam = {
        'state': 'favTeam',
        '`Who\'s your favorite professional player?`': {
            '[{faker}]':{ #$FAV_PLAYER
                'state':'teamCondition',
                '`What do you think about how they\'ve been doing lately?`': {
                   '[{good, well, great, decent, nice, okay}]': {
                        '`That\'s valid, but I think (fav player) was better in YEAR`':'end'
                    },
                    '[{hasnt, not, bad}]':{
                        '`I agree. (fav player) was much better before`': 'end'
                    },
                    'error':{
                        '`what.`':'end' #error condition not handled
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