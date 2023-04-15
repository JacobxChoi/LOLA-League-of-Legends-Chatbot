def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '#GATE`I\'ll share some of my personal favorites. Keria is my favorite player, but my favorite team is Edward Gaming. They\'re very fun to watch.`': { #user will ask questions
            # 'score': 0.9,
            'state':'share',
            '{[like, {edg, them, team}]}': 'EDG', #USER: I like them too!
            '{[like, {keria, him}]}': {  # USER: I like them too!
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
                                                            'state': 'somethingElse',
                                                            '{team, teams}': {
                                                                '`What team do you wanna talk about then?`': 'describeTeam' #TODO
                                                            },
                                                            '{[{recent, recently, past}, {match, game}]}': {
                                                                '`Which match?`': 'describeMatch' #TODO
                                                            },
                                                            '{information, info, game, match, league, lol}': {
                                                                '`What part of league do you want to talk about?`': 'describeLeague' #TODO
                                                            },
                                                            '{no, not, nah, pass, [im, {good, fine}]}': {
                                                                '`I\'ll see you later then! Bye!`': 'end'
                                                            },
                                                            '{yes, ok, yeah, sure, fun, alright, cool, [sounds, {fun, good}]}': {
                                                                '`What do you wanna talk about then?`': 'somethingElse'
                                                            },
                                                            '#UNX': {
                                                                '`I\'ll see you later then! Bye!`': 'end'
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
        '#GATE`Are there any games or tournaments that you watched this year?`': {
            # 'score': 0.9,
            '[{yes, yeah, watched, watch}]': { #USER: yeah! this year, I watched a game between team1 and team2
                '`That\'s cool! Who was the highlight of the game?`': {
                    '[$HIGHLIGHT_PLAYER = #ONT(teams)]': {
                        '`I agree!` $HIGHLIGHT_PLAYER `has been doing well lately. Do you think they\'ll continue to do well?`':{
                            '[{yes, well}]': {
                                '`I agree! Their stats are above average this season, and I think they will help their team go far!`':'casual' #TODO: CONTRADICTION, BECAUSE NO API
                            },
                            '[{no, wont, disagree, [definitely, not], [absolutely, not]}]': {
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
                    '[{no, not, wasnt}]':{ #USER: no, the game wasnt really close
                        '`Dang. I\'m not a fan of one-sided games either.`':'end'
                    }
                }
            },
            '[{no, did not, didnt}]':{
                '`No worries!`':'casual'
            },
            'error':'end'
        }, #TODO: handle gate
        '`End of gate`':{
            'score':0.1,
            'state':'end'
        }
    }
    edg = {
        'state': 'EDG',
        '`Awesome! What do you like about Edward Gaming?`': {
            'state': 'EDG2',
            '[{skill, macro, macroplay, strategy, skillful, skilled, dynamic}]': {
                '`I also think that they\'re really skillful and smart at strategizing. I mean, they have to be in order to win '
                'Worlds. I think that they win because of their ability to adapt to new scenarios.`': {
                    '[{agree, also, too, true}]': {
                        '`I\'m glad to hear you think the same way! Is there another reason why you like them?`': {
                            '[{yes, yeah, sure, of course, do}]': {
                                '`What is it?`': 'EDG2'
                            },
                            '[{no, not, nah, dont}]': {
                                '`That\'s valid. It was nice talking to you! See ya soon!`' 'end' #we should make a state that prompts the user whether or not they want to talk about a region or team or player
                            },
                            '[{fun, entertaining, fast, fast paced, action, engaging}]': {
                                '`Yeah. Since they\'re accustomed to action-packed games, they\'re able to overwhelm the'
                                ' enemy team by playing proactively. On the other hand, what do you think about their '
                                'fanbase community?`': {
                                    '[{good, fantastic, nice, home, fun, welcoming, energetic, best, like}]': {
                                        '`They naturally will have a strong community because they\'re such a good team. Their '
                                        'fan base is the best, probably because I\'m a part of it. I\'m glad that we'
                                        ' both have similar taste in pro teams. I\'ll see you later! Bye!`': 'end'
                                    },
                                    '[{bad, worst, not good, poor, toxic, boring, dead, dislike, hate}]': {
                                        '`That makes me sad to hear because I\'m a part of it and I love it :(. Try it out again and'
                                        ' see if you change your mind. It was still nice talking to you. Bye!`': 'end'
                                    },
                                    'error': {
                                        '`That\'s alright. Hopefully you\'ll join me and the others after watching some'
                                        ' more games. I\'ll catch you later!`': 'end'
                                    }

                                }
                            },
                            '[{fans, fanbase, community}]': {
                                '`For sure!. They naturally will have a strong community because they\'re such a good team. Their '
                                'fan base is the best, probably because I\'m a part of it. On the other hand, what do'
                                ' you think about the way they play?`': {
                                    '[{strong, good, best, strongest, fun, entertaining, fast, fast paced, action, engaging}]': {
                                        '`I agree. They probably have a strong fan base because of how good they are. It'
                                        ' was nice talking to you,'
                                        ' and I\'m glad we share similar interests!`': 'end'
                                    },
                                    '[{bad, worst, not good, poor, boring, dislike, weak}]' : {
                                        '`Really? I really like the way that they play. You should go check out some of '
                                        'their games in the LPL. That might change your mind. I\'ll see you later!`': 'end'
                                    },
                                    'error': {
                                        '`I hope you continue to watch EDG\'s games and cheer them on as a fan! See ya!`': 'end'
                                    }

                                }
                            },
                            'error': {
                                '`That\'s valid. It was nice talking to you! See ya soon!`': 'end'
                            }
                        }
                    }
                }
            },
            '[{fun, entertaining, fast, fastpaced, action, engaging}]': {
                '`Yeah. Since they\'re accustomed to action-packed games, they\'re able to overwhelm the enemy team with their proactive play.`': {
                    '[{agree, also, too, true}]': {
                        '`I\'m glad to hear you think the same way! Is there another reason why you like them?`': {
                            '[{yes, yeah, sure, of course, do}]': {
                                '`What is it?`': 'EDG2'
                            },
                            '[{no, not, nah, dont}]': {
                                '`That\'s valid. It was nice talking to you! See ya soon!`' 'end'
                                # we should make a state that prompts the user whether or not they want to talk about a region or team or player
                            },
                            '[{skill, macro, macroplay, strategy, skillful, skilled}]': {
                                '`Of course! They\'re a super solid team that is really good at making plays together as a team. '
                                'On the other hand, what do you think about their fanbase community?`': {
                                    '[{good, fantastic, nice, home, fun, welcoming, energetic, best, like}]': {
                                        '`They naturally will have a strong community because they\'re such a good team. Their '
                                        'fan base is the best, probably because I\'m a part of it. I\'m glad that we'
                                        ' both have similar taste in pro teams. I\'ll see you later! Bye!`': 'end'
                                    },
                                    '[{bad, worst, not good, poor, toxic, boring, dead, dislike, hate}]': {
                                        '`That makes me sad to hear because I\'m a part of it and I love it :(. Try it out again and'
                                        ' see if you change your mind. It was still nice talking to you. Bye!`': 'end'
                                    },
                                    'error': {
                                        '`That\'s alright. Hopefully you\'ll join me and the others after watching some'
                                        ' more games. I\'ll catch you later!`': 'end'
                                    }

                                }
                            },
                            '[{fans, fanbase, community}]': {
                                '`They naturally will have a strong community because they\'re such a good team. Their '
                                'fan base is the best, probably because I\'m a part of it. On the other hand, who\'s your'
                                ' favorite player on EDG?`': { #TODO
                                    'state': 'playerEDG',
                                    '[{ale, jia le, jiale, top}]': {
                                        '`That\'s a strong choice. I think he\'s a really talented top laner. EDG Meiko '
                                        'is still my favorite player on this team though. I think you should focus on him too.`': 'end' #TODO
                                    },
                                    '[{jiejie, li jie, lijie, jungle, jungler}]': {
                                        '`That\'s a strong choice. I think he\'s a really talented jungler. His ganks '
                                        'always seems to work. EDG Meiko is still my favorite player on this team '
                                        'though. I think you should focus on him too.`': 'end' # TODO
                                    },
                                    '[{fofo, chun lan, chunlan, mid, middle, midlaner}]': {
                                        '`That\'s a strong choice. I think he\'s a really good midlaner. His roam '
                                        'timings and laning is strong. EDG Meiko is still my favorite player on this team '
                                        'though. I think you should focus on him too.`': 'end' # TODO
                                    },
                                    '[{leave, hong chao, hongchao, bot, adc, bottom, botlaner}]': {
                                        '`That\'s an interesting choice. I think he\'s a really good adc. His team-fighting '
                                        'and laning is really strong. EDG Meiko is still my favorite player on this team '
                                        'though. He makes Leave seem a lot stronger in lane.`': 'end'  # TODO
                                    },
                                    '[{meiko, tian ye, ye, sup, support}]': {
                                        '`Wow! He\'s also my favorite player on EDG! What makes you think he\'s so good?'
                                        ' I like him cause of his laning phase.`': 'end'  # TODO
                                    },
                                    '[{monki, meng qi, mengqi, jungle, jungler}]': {
                                        '`Wow! That is a very interesting choice. I didn\'t expect you to say a '
                                        'substitute player! You must really watch EDG.`': 'end'  # TODO
                                    },
                                    '[{fisher, jeong tae, jeongtae, mid, middle, midlane, midlaner}]': {
                                        '`Wow! That is a very interesting choice. I didn\'t expect you to say a '
                                        'substitute player! You must really watch EDG.`': 'end'  # TODO
                                    },
                                    'error': {
                                        '`I don\'t think that person currently plays for EDG. Try another player.`': 'playerEDG'
                                    }
                                }
                            },
                            'error': {
                                '`That\'s valid. It was nice talking to you! See ya soon!`': 'end'
                            }
                        }
                    }
                }
            },
            '[{fans, fanbase, community}]': {
                '`They naturally will have a strong community because they\'re such a good team. Their fanbase is the '
                'best, probably because I\'m a part of it. What do you like about it?`': {
                    '[{good, agree, dont disagree, fantastic, nice, home, fun, welcoming, energetic, best, like}]': {
                        '`Yeah, I think that we\'re the best. I\'ll see you later! Bye!`': 'end'
                    },
                    '[{bad, disagree, dont agree, worst, not good, poor, toxic, boring, dead, dislike, hate}]': {
                        '`That makes me sad to hear because I\'m a part of it and I love it :(. Try it out again and'
                        ' see if you change your mind. It was still nice talking to you. Bye!`': 'end'
                    },
                }
            },
            '[{ale, jia le, jiale, top}]': {
                '`That\'s a strong choice. I think he\'s a really talented top laner. EDG Meiko'
                ' is still my favorite player on this team though. I think you should focus on him too.`': 'end'  # TODO
            },
            '[{jiejie, li jie, lijie, jungle, jungler}]': {
                '`Awesome!. I think Jiejie\'s a really talented jungler. His ganks '
                'always seems to work. EDG Meiko is still my favorite player on this team '
                'though. I think you should focus on him too.`': 'end'  # TODO
            },
            '[{fofo, chun lan, chunlan, mid, middle, midlaner}]': {
                '`That\'s a strong choice. I think he\'s a really good midlaner. His roam '
                'timings and laning is strong. EDG Meiko is still my favorite player on this team '
                'though. I think you should focus on him too.`': 'end'  # TODO
            },
            '[{leave, hong chao, hongchao, bot, adc, bottom, botlaner}]': {
                '`That\'s an interesting choice. I think he\'s a really good adc. His team-fighting '
                'and laning is really strong. EDG Meiko is still my favorite player on this team '
                'though. He makes Leave seem a lot stronger in lane.`': 'end'  # TODO
            },
            '[{meiko, tian ye, ye, sup, support}]': {
                '`Wow! He\'s also my favorite player on EDG! What makes you think he\'s so good?'
                ' I like him cause of his laning phase.`': 'end'  # TODO
            },
            '[{monki, meng qi, mengqi, jungle, jungler}]': {
                '`Wow! That is a very interesting choice. I didn\'t expect you to say a '
                'substitute player! You must really watch EDG.`': 'end'  # TODO
            },
            '[{fisher, jeong tae, jeongtae, mid, middle, midlane, midlaner}]': {
                '`Wow! That is a very interesting choice. I didn\'t expect you to say a '
                'substitute player! You must really watch EDG.`': 'end'  # TODO
            },
            'error': {
                '`I don\'t think that person currently plays for EDG. Try another player.`': 'playerEDG'
            }
        }
    }
    return casual, edg

#TODO connect these to convo.py

def favPlayer(): #TODO: WE ALREADY HAVE FAVPLAYER VAR
    favPlayer = {
        'state': 'favPlayer'
    }
    return favPlayer