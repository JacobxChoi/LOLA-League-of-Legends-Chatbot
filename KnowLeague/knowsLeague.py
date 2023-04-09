
def knowsLeague():
    favoriteTeam = {
        'state': 'favPlayer',
        '`Who\'s your favorite professional player?`': {
            'state': 'playerCondition',
            '[keria]':{
                '`I agree! I love keria too!`': 'keria'
            },
            '[$FAV_PLAYER=#ONT(leagues)]':{
                '`How do you think` $FAV_PLAYER `has been doing lately?`': {
                   '[{good, well, great, decent, nice, okay, not bad, better}]': {
                        '`That\'s valid. I would say that keria is probably doing the best right now though.`':{
                            '[{agree, right, yeah}]':'end',
                            '[{nah, dont, no, disagree}]':'end',
                            '[{why}]':'end'
                        },
                       'error':'end'
                    },
                    '[{hasnt, not, bad, worse}]':{
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
        'state': 'favRegion',
        '`How about a favorite region to watch?`':{
            'state':'favRegion2',
            '#FAV_REGION':{ #TODO handle case where user doesn't have favorite region
                '`Did you watch the`$T_TOURNEY $T_MATCH `where` $T_WINNER `beat` $T_LOSER `?`': {
                    '[{yes, did, watched}]':'advanced', #shows that user actively watches current esports games.
                    '[{no, [did not], dont, didnt}]':{ #next favorite region?
                        '`No Worries. How about this other match?`':{
                            '[{yes, yeah, watch, watched}]':'advanced',
                            '[{no, [did not], didnt, havent, [have not]}]':{ #perhaps they're not watching current games. This will prompt them into the casual branch
                                '`All good!`':'casual'
                            },
                            'error':'end'
                        }
                    }, #TODO user responds with "I didn't watch, but I know the outcome
                    'error':'end'
                }
            },
            'error':{ #TODO: FIX TRANSITION
                '`Sorry, I\'m not sure if I know that region. Is there another region you might watch?`':'favRegion2'
            }
        }
    }
    return favoriteTeam, favoriteRegion