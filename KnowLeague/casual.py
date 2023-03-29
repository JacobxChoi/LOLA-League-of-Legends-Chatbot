def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '#GATE`I\'ll share some of my favorite teams. Jojopyun is my favorite player, but my favorite team is Edward Gaming. They\'re fun to watch`': { #user will ask questions
            '{[like, too]}':{#USER: I like them too!
                '`Awesome! What do you like about Edward Gaming?`':'EDG'
            },
            '[{like}]':{ #USER: What do you like about them?
                '`I like how they\'re very aggressive. They hardly make mistakes, and they\'re really fun to watch. What do you think?`':{
                    '[{like}]':{ #I like Edward Gaming too!
                        '`nice!`':'end'
                    },
                    '[{think}]':{ #I think they're good too, but I prefer ...
                        '`That\'s fair.`':'end'
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
            'error':'end'
        },
        # USER didn't watch Lola suggested games, but perhaps they still watched a game from this year
        '#GATE`Are there any games or tournaments that you watched this year?`':{
            '[{yes, yeah, watched, watch}]':{ #USER: yeah! this year, I watched a game between team1 and team2
                '`That\'s cool! Who was the highlight of the game?`' :{

                },
                '`Nice! Who won the game? Was it close?`':{
                    '[{yes, yeah, close}]':{ #USER: yeah, it was a really close game!
                        '`awesome!`':'end'
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
        }, #TODO: move gate to different part of conversation
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

def favTeam():
    favTeam = {
        'state': 'favTeam'
    }
    return favTeam

def favPlayer():
    favPlayer = {
        'state': 'favPlayer'
    }
    return favPlayer