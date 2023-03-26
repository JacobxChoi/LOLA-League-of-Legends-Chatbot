
def knowsLeague():
    favoriteTeam = {
        'state': 'favPlayer',
        '`Who\'s your favorite professional player?`': {
            'state': 'playerCondition',
            '[jojopyun]':{
                '`I agree! I love jojopyun too!`':'end'
            },
            '[$FAV_PLAYER=#ONT(leagues)]':{
                '`How do you think` $FAV_PLAYER `has been doing lately?`': {
                   '[{good, well, great, decent, nice, okay, not bad}]': {
                        '`That\'s valid. I would say that jojopyun is probably doing the best right now though.`':{
                            '[{agree, right, yeah}]':'end',
                            '[{nah, dont, no, disagree}]':'end',
                            '[{why}]':'end'
                        },
                       'error':'end'
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
            '#FAV_REGION':{
                '`Did you watch the` $T_TOURNEY':'end' #leads to open ended response
            },
            'error':'end'
        }
    }
    return favoriteTeam, favoriteRegion