
def knowsLeague():
    favoriteTeam = {
        'state': 'favPlayer',
        '`Do you have a favorite professional player, and what do you think about them?`': {
            'state': 'playerCondition',
            '[{keria}]': 'keria',
            # '[{no, not, dont, cant, none, nothing}]': {
            #     '`No worries.`': 'casual'
            # },
            '[$FAV_PLAYER=#ONT(leagues), {bad, terrible, [not good], [not doing well], [not doing good], [not been doing well], [not been doing well lately], [not been doing too well], [not been doing good], [not been doing too good]}]':{
                '`Why do you think` $FAV_PLAYER `has been doing poorly?`': {
                    'error': {
                        '`That\'s true. I think`$FAV_PLAYER`Could be doing better as well. Do you watch any tournaments?`':'favRegion'
                    }
                }
            },
            '[$FAV_PLAYER=#ONT(leagues), {good, well, okay, great, amazing}]': {
                '`I agree. I think`$FAV_PLAYER`is doing pretty well too. Do you watch any tournaments?`':'favRegion'
            },
            '[{like}, $FAV_PLAYER=#ONT(leagues)]': {
                '`I love` $FAV_PLAYER `too. Do you watch any tournaments?`': 'favRegion'
            },
            '[$FAV_PLAYER=#ONT(leagues)]':{
                'score': 0.9,
                '`What do you like about`$FAV_PLAYER':{
                    '[{good, well, plays, capable, knows, [not bad]}]':{
                        '`I agree,` $FAV_PLAYER `is one of the most skilled players out there. How do you think they\'ll do in the future?`':{
                            'state':'playerFuture',
                            '[{okay, well, good, decent}]':{
                                '`I agree. I think they\'ll go pretty far.`': 'casual'
                            },
                            '[{retire, retiring}]':{
                                '` They will be missed. :( Is there anything else about esports that interests you?`': 'favRegion'
                            },
                            '[{bad, poor, wont, dont}]':{
                                '`Maybe not, but it\'s difficult to tell now. I hope they improve, or that they\'ll work something out. Is there anything else about esports that interests you?`':'favRegion'
                            },
                            '[{[dont know], [not sure], unsure}]':{
                                '`That\'s fair. Anything could happen in the future. I hope they\'re still enjoying the game. Is there anything else about esports that interests you?`':'favRegion'
                            },
                            'error':{
                                '`I\'m sorry, could you rephrase what you just said?`':'playerFuture'
                            }
                        }
                    },
                    '[{bad, terrible, [not good], [not doing well], [not doing good], [not been doing well], [not been doing well lately], [not been doing too well], [not been doing good], [not been doing too good]}]':{

                    },
                    'error':{
                        '`Nice. Do you follow any tournaments?`': 'favRegion'
                    }
                }
            },
            '[{no, dont have, do not, dont}, player]':'favRegion',
            'error':'favRegion' #if user doesn't have favorite player, go to favorite region
        }
    }
    favoriteRegion = { #
        'state': 'favRegion',
        '`What about a favorite region to watch?`':{
            'state':'favRegion2',
            '[yes, yeah]':{
              '`What region do you watch?`':'favRegion2'
            },
            '[no, not, dont]':'noFavRegion',
            '#FAV_REGION':{
                'state':'favRegion2Test',
                '`Did you watch the`$T_TOURNEY $T_MATCH `where` $T_WINNER `beat` $T_LOSER `?`': {
                    'state':'firstSuggestion',
                    '[{yes, yeah, watched, probably, yea, maybe}]':'advanced', #shows that user actively watches current esports games.
                    '[{no, [did not], didnt, havent, [have not], nope, dont}]':{ #next favorite region?
                        '#RANDGAME `No Worries. How about the `$T_TOURNEY $T_MATCH `game where` $T_WINNER `beat` $T_LOSER `?`':{
                            'state':'secondSuggestion',
                            '[{yes, yeah, watch, watched, probably, yea, maybe}]':'advanced',
                            '[{no, [did not], [didnt watch], [havent watched], [have not], nope, dont}]':{ #perhaps they're not watching current games. This will prompt them into the casual branch
                                'state':'noFavRegion',
                                '`All good!`':'casual'
                            },
                            'error':{
                                '`Sorry, could you rephrase what you said?`': 'secondSuggestion'
                            }
                        }
                    },
                    '[{outcome, wins}]':{ #i didn\'t watch, but I know who wins
                        '`That\'s awesome. Yeah, it was cool to see` $T_WINNER `win`#RANDGAME `Did you also happe to watch the `$T_TOURNEY $T_MATCH `game where` $T_WINNER `beat` $T_LOSER `?`': 'secondSuggestion'
                    },
                    'error':{
                        '`Sorry, could you rephrase what you said?`':'firstSuggestion'
                    }
                }
            },
            '[{no, not, dont, doesnt, nah}]': {
                '`That\'s all good.`': 'casual'
            },
            'error':{
                '`Sorry, I don\'t remember any games from that region this year. Is there another region you might watch?`':'favRegion2'
            }
        }
    }
    return favoriteTeam, favoriteRegion