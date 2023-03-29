
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
            '[{no, dont have, do not, dont}]':'favRegion',
            'error':'favRegion' #if user doesn't have favorite player, go to favorite region
        }
    }
    favoriteRegion = { #
        'state':'favRegion',
        '`What\'s your favorite region to watch?`':{
            '#FAV_REGION':{ #TODO handle case where user doesn't have favorite region
                '`Did you watch the`$T_TOURNEY $T_MATCH `between` $T_TEAM1 `and` $T_TEAM2 `where` $T_WINNER `won?`': {
                    '[{yes, did, watched}]':'advanced', #shows that user actively watches current esports games.
                    '[{no, did not, didnt}]':{ #next favorite region?
                        '`No Worries. How about this other match?`':{
                            '[{no, did not, didnt, havent, have not}]':{ #perhaps they're not watching current games. This will prompt them into the casual branch
                                '`All good!`':'casual'
                            },
                            'error':'end'
                        }
                    }, #TODO user responds with "I didn't watch, but I know the outcome
                    'error':'end'
                }
            },
            'error':'end'
        }
    }
    return favoriteTeam, favoriteRegion