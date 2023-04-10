def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '#GATE`I\'ll share some of my personal favorites. Keria is my favorite player, but my favorite team is Edward Gaming. They\'re fun to watch`': { #user will ask questions
            # 'score': 0.9,
            'state':'share',
            '{[like, {EDG, them, team}, too]}':{#USER: I like them too!
                '`Awesome! What do you like about Edward Gaming?`':'EDG'
            },
            '{[like, {keria, him}, {too, also}]}': {  # USER: I like them too!
                '`Awesome! What do you like about Keria?`': 'keria'
            },
            '{[you, like]}':{ #USER: What do you like about them?
                '`I like how they\'re very aggressive. They hardly make mistakes, and they\'re really fun to watch. What about you?`':{
                    '{[like,{too, also}], [also, like]}':{ #I like Edward Gaming too!
                        '`Nice! Do you like them for their personality or gameplay?`': {
                            '[{playstyle, play, style, skills, abilities, gameplay}]': {
                                '`What do you like about it specifically?`': {
                                    '[{aggressive, fastpaced, fun, skilled, flashy, technical, informational, fast paced}]': {
                                        '`If you like that then you should also check out T1! They\'re really calculated in their plays.`': {
                                            '{[already, watch],[watch, already]}': {
                                                '`Nice! Do you want any more similar suggestions?`': {
                                                    '{yes, ok, yeah, sure, fun, alright, [sounds, {fun, good}]}': {
                                                        '`Check out FNC\'s game against GAM during the 2017 World\'s '
                                                        'group stage. It had one of the craziest starts to a game I have ever seen.`': {
                                                            '{why, how, what}': {
                                                                '`By the time one jungler was level six, the enemy top '
                                                                'laner was only level two. I won\'t spoil the rest of '
                                                                'the game so you should give it a watch. '
                                                                'Is there anything else you wanted to talk about?`': {

                                                                }
                                                            },
                                                            '{yes, ok, yeah, sure, fun, alright, cool, [sounds, {fun, good}]}': {
                                                                #TODO: Store the match
                                                                '`Alrighty! Let me know what you think of it later!`': 'end'
                                                            },
                                                            '{no, not, nah, pass, [im, {good, fine}]}': {
                                                                '`Oh, ok... Do you want another game or team to watch?`': {
                                                                    '#RANDGAME':{
                                                                        'state':'suggestGame',
                                                                        '`Sure, how about the`$T_TOURNEY $T_MATCH `game where` $T_WINNER `beat` $T_LOSER `?`':{
                                                                            '[no, dont]':'suggestGame',
                                                                            '[yes, yeah]':'end'
                                                                        }
                                                                    },
                                                                    'error':'end' #user doesn't say 'yes' or 'yeah' TODO: use chatgpt to handle user input
                                                                }
                                                            },
                                                            'error': {
                                                                '`Okay I gotcha.`': 'end'
                                                            }
                                                        }
                                                    },
                                                    '{no, not, nah, pass, [im, {good, fine}]}': {
                                                        '`Alrighty! I\'ll see you later!`': 'end'
                                                    }
                                                },
                                                '{no, not, nah, pass, [im, {good, fine}]}': {
                                                        '`Then do you want to talk about something else? I mainly can '
                                                        'talk about teams, recent games, and information about the game`': {
                                                            '{team, teams}': {

                                                            }
                                                        }
                                                    }
                                            },
                                            '{yes, ok, yeah, sure, fun, alright, [sounds, {fun, good}]}': {

                                            }
                                        },
                                    },
                                    'error': {
                                        '`Awesome! Are there any other players you enjoy watching?`': 'favPlayer'
                                    }
                                }
                            },
                            '[{personalities, personality, character, charisma}]': {
                                '`In what way?`': {

                                }
                            }
                        }
                    },
                    '[{agree}]': {
                        '`Awesome! Happy to hear you think that way.`'
                    },
                    '[{think}]':{ #I think they're good too, but I prefer ...
                        '`That\'s fair.`':'end' #TODO
                    },
                    'error':'end'
                }
            },
            '{[favorite, team]}':{ #USER: my favorite team is ___
                '`What do you like about your favorite team?`':'favTeam'
            },
            '{[think]}': {  # USER: I think _____ team is better, though
                '`What do you like about this team?`': 'favTeam'
            },
            '{[favorite, player]}':{ #USER: my favorite player, though, is _____
                '`What do you like about them?`':'favPlayer'
            },
            'error':'share'
        },
        # USER didn't watch Lola suggested games, but perhaps they still watched a game from this year
        '#GATE`Are there any games or tournaments that you watched this year?`':{
            # 'score': 0.9,
            '[{yes, yeah, watched, watch}]':{ #USER: yeah! this year, I watched a game between team1 and team2
                '`That\'s cool! Who was the highlight of the game?`' :{
                    '[$HIGHLIGHT_PLAYER = #ONT(teams)]':{
                        '`I agree!` $HIGHLIGHT_PLAYER `has been doing well lately. Do you think they\'ll continue to do well?`':{
                            '[{yes, well}]':{
                                '`I agree! Their stats are above average this season, and I think they will help their team go far!`':'casual' #TODO: CONTRADICTION, BECAUSE NO API
                            },
                            '[{no, wont, disagree, [definitely, not], [absolutely, not]}]':{
                                '`I see. Their stats are below average this season, so maybe they won\'t do too well.`':'casual' #LOOPS BACK TO BEGINNING OF CONVO
                            },
                            'error':'end' #TODO: HANDLE ERROR
                        }
                    },
                    'error': 'end'
                },
                '`Nice! Who won the game? Was it close?`':{
                    '[{yes, yeah, close}]':{ #USER: yeah, ___ won, and it was a really close game!
                        '`Wow! I\'m sure TEAM put up a really good fight.`':'end' #TODO: HANDLE ERROR
                    },
                    '[{no, not}]':{ #USER: no, the game wasnt really close
                        '`Dang. I\'m not a fan of one-sided games either.`':'end'
                    }
                }
            },
            '[{no, did not, didnt}]':{
                '`no worries!`':'casual'
            },
            'error':'end'
        }, #TODO: handle gate
        '`End of gate`':{
            'score':0.1,
            'state':'end'
        }
    }
    return casual

#TODO connect these to convo.py

def EdwardGaming():
    EDG = {
        'state': 'EDG'
    }
    return EDG

def Keria():
    Keria = {
        'state': 'keria'

    }
    return Keria
def favTeam():
    favTeam = {
        'state': 'favTeam'
    }
    return favTeam

def favPlayer(): #TODO: WE ALREADY HAVE FAVPLAYER VAR
    favPlayer = {
        'state': 'favPlayer'
    }
    return favPlayer