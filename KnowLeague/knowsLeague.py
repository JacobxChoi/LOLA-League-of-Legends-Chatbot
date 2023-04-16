
def knowsLeague():
    favoriteTeam = {
        'state': 'favPlayer',
        '`Who\'s your favorite professional player, and what do you think about them?`': {
            'state': 'playerCondition',
            '[keria]':{
                '`I agree! I love keria too!`': 'keria'
            },
            '[$FAV_PLAYER=#ONT(leagues), {bad, terrible, [not good], [not doing well], [not doing good], [not been doing well], [not been doing well lately], [not been doing too well], [not been doing good], [not been doing too good]}]':{
                '`Why do you think` $FAV_PLAYER `has been doing poorly?`': { #TODO: CONTINUE WORKING ON THIS CONVERSATION
                   '[{stats}]':{ #his stats have not been too good #TODO ANOTHER CHANCE TO SHOWCASE STATS HERE
                        '`that\'s fair`':'end'
                   },
                    'error':'end'
                }
            },
            '[$FAV_PLAYER=#ONT(leagues), {good}]': {
                '`Why do you think` $FAV_PLAYER `has been doing good lately? `':{
                    'error':'end'
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
                        '#RANDGAME `No Worries. How about the `$T_TOURNEY $T_MATCH `game where` $T_WINNER `beat` $T_LOSER `?`':{
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