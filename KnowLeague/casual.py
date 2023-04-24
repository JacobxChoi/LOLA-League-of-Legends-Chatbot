def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '#GATE`I\'ll share some of my personal favorites. Keria is my favorite player, but my favorite team is Edward Gaming. They\'re very fun to watch.`': { #user will ask questions
            'score': 0.6,
            'state':'share',
            '{<{like,love}, {edg, them, team, edward}>}': 'EDG', #USER: I like them too!
            '[{keria, him, he}]': 'keria',
            '{[{what, why}, you, like]}':{ #USER: What do you like about them?
                '`I like how they\'re very aggressive. They hardly make mistakes, and they\'re really fun to watch. What about you?`':{
                    'state':'LolaLikesEDG',
                    '{<{like, watch, prefer}, {too, also}>}':{ #I like Edward Gaming too!
                        'state':'reciprocateEDG',
                        '`Do you like them for their personality or gameplay?`': {
                            '[{playstyle, play, style, skills, abilities, gameplay}]': {
                                '`What do you like about it specifically?`': {
                                    '[{aggressive, fastpaced, fun, skilled, flashy, technical, informational, fast paced}]': {
                                        '`If you like that then you should also check out T1! They\'re really calculated in their plays.`': {
                                            'state': 'watchT1',
                                            '{<already, {watch, watched, know}>, have}': {
                                                '`Nice! Do you want any more similar suggestions?`': {
                                                    '{yes, ok, yeah, sure, fun, alright, [sounds, {fun, good}]}': {
                                                        '`Check out FNC\'s game against GAM during the 2017 World\'s group stage. '
                                                        'It had one of the craziest starts to a game I have ever seen.`': {
                                                            '{why, how, what}': {
                                                                '`By the time one jungler was level six, the enemy top laner was only level two. '
                                                                'I won\'t spoil the rest of the game, but you should give it a watch.`': { #TODO: EXAPND CONVO
                                                                    '[{nope, no, not, cant, wont, dont, cannot}]': {
                                                                        '`Alrighty. I really think you should give it a watch. Have a good rest of your day!`': 'end'
                                                                    },
                                                                    '[{yes, yeah, ok, sure, watch}]': {
                                                                        '`Nice! I hope you have a good time. Bye bye!`': 'end'
                                                                    }

                                                                },
                                                                'error':'end'
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
                                                                '`Okay I gotcha.`': 'end' #TODO: EXPAND CONVO
                                                            }
                                                        }
                                                    },
                                                    '[{no, not, nah, pass, im good, im fine, i am good, i am fine}]': { #TODO: EXPAND CONVO
                                                        '`Alrighty! I\'ll see you later!`': 'end'
                                                    }
                                                },
                                                '{no, not, nah, pass, [im, {good, fine}]}': {
                                                        '`Then do you want to talk about something else? I mainly can talk about teams, recent games, and information about the game`': {
                                                            'state': 'somethingElse',
                                                            '{team, teams}': {
                                                                '`What team do you wanna talk about then?`': 'describeTeam' #TODO
                                                            },
                                                            '{[{recent, recently, past}, {match, game}]}': {
                                                                '`Which match?`': 'describeMatch' #TODO EXPAND CONVO
                                                            },
                                                            '{information, info, game, match, league, lol}': {
                                                                '`What part of league do you want to talk about?`': 'describeLeague' #TODO
                                                            },
                                                            '{no, not, nah, pass, [im, {good, fine}]}': { #TODO: REROUTE CONVO
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
                                                '`Come back after you check them out! I\'ll catch ya later!`':'end'
                                            },
                                            'error': {
                                                '`I\'m not sure if I caught that, can you reword it?`': 'watchT1'
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
                                    'error': {
                                        '`Are there any videos where I can see their personalities?`': {
                                            'error': {
                                                '`Gotcha. I didn\'t know that about them. They seem like a lot of fun. '
                                                'As a matter of fact, I\'ll go check them out right now. See ya!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[{agree}]': {
                        '`Awesome! Happy to hear you think that way.`':'reciprocateEDG'
                    },
                    '[like, more]':{ #I like ____ more.
                        '`That\'s fair.`':'favTeamQuestion'
                    },
                    '[prefer]':{ #I prefer _____
                        '`That\'s fair.`': 'favTeamQuestion'
                    },
                    '[dont, disagree, dislike]':{ #I don't really watch EDG
                        '`That\'s fair. What are your thoughts on Keria then. Do you like him?`':{
                            'state':'thoughtsOnKeria',
                            '[yes, like, good, skilled]':'keria',
                            '[no, dislike, dont, not]':{
                                '`Do you have a favorite team, then?`':{
                                    'state':'otherFavTeam',
                                    '[yes, yeah, [I do], yep, yea]':'favTeamQuestion',
                                    '[no, nope, [do not], dont]':{
                                        '`What other player do you think is currently good at the moment then?`':'otherPlayer',
                                    },
                                    'error':{
                                        '`I\'m sorry, would you mind rewording that?`':'otherFavTeam'
                                    }
                                }
                            },
                            'error':{
                                '`I\'m sorry, would you mind rewording that?`': 'thoughtsOnKeria'
                            }
                        }
                    },
                    'error':{
                        '`I\'m sorry, I didn\' catch that. Could you reword that?`':'LolaLikesEDG'
                    }
                }
            },
            '{[favorite, team]}':{ #USER: my favorite team is ___
                'state':'favTeamQuestion',
                '`What do you like about your favorite team?`':'favTeam'
            },
            '[$FAV_PLAYER=#ONT(leagues), {better, more}]':{ #USER: my favorite player, though, is _____
                'state':'otherPlayer',
                '`What do you like about them?`': {
                    '[{skilled, good, talented}]':{
                        '`I agree. I think`$FAV_PLAYER`is really capable too. How does he compare with other players?`':{
                            '[{better, capable, skilled}]':{
                                '`That\'s fair. I still think Keira is the best though. His ability to carry the team is unparalleled.`':'end'
                            },
                            '[{worse, unskilled, [as good]}]':{ #TODO: FINISH
                                '``'
                            }
                        }
                    }
                }
            },
            '[no, not, cant, wont, dont]':{ #I don't really watch keria or EDG
                '`No worries. What other teams do you prefer watching?`':{ #TODO: FINISH

                }
            },
            'error': 'casual'
        },
        # USER didn't watch Lola suggested games, but perhaps they still watched a game from this year
        '#GATE`By the way, are there any games or tournaments that you watched this year?`':{
            'score': 0.5,
            '[{yes, yeah, watched, watch}]':{ #USER: yeah! this year, I watched a game between team1 and team2
                '`That\'s cool! Who was the highlight of the game?`': {
                    'state': 'testing',
                    #'state':'highlight',
                    '[$HIGHLIGHT_PLAYER = #ONT(teams)]':{
                        '`I agree!` $HIGHLIGHT_PLAYER `has been doing well lately. Do you think they\'ll continue to do well?`':{
                            'state':'playerWellness',
                            '[{yes, well}]':{
                                '`I agree! Their stats are above average this season, and I think they will help their team go far!`':'casual' #TODO: CONTRADICTION, BECAUSE NO API
                            },
                            '[{no, wont, disagree, [definitely, not], [absolutely, not]}]':{
                                '`I see. Their stats are below average this season, so maybe they won\'t do too well.`':'casual' #LOOPS BACK TO BEGINNING OF CONVO
                            },
                            'error':{
                                '`I\'m, sorry, I didn\'t quite get that. Could you reword what you just said?`':'playerWellness'
                            }
                        }
                    },
                    'error': {
                        '`Sorry, I don\'t think I know that player. Do you have someone else in mind?`':'highlight'
                    }
                },
                '`Nice! Who won the game? Was it close?`':{
                    'score': 2.0,

                    '[$WINNINGTEAM=#ONT(teams),{beat, won, defeated}]':{ #USER: yeah, ___ won, and it was a really close game!
                        '`Wow! I\'m sure that was a really satisfying win for`$WINNINGTEAM`.`':'end' #TODO: HANDLE ERROR
                    },
                    '[{no, not, wasnt}]':{ #USER: no, the game wasnt really close
                        '`Dang. I\'m not a fan of one-sided games either.`':'end'
                    }
                }
            },
            '[{no, not, nope, cannot, didnt, cant, wont, dont}]':{
                '`That\'s a shame, I don\'t have much to talk about then. Try coming back after watching a game so that we can talk! See ya!`':'end'
            },
            'error':'end'
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
                                        '`That\'s a strong choice. I think he\'s a really talented top laner. EDG Fofo '
                                        'is still my favorite player on this team though. I think you should check him out too.`': 'end' #TODO
                                    },
                                    '[{jiejie, li jie, lijie, jungle, jungler}]': {
                                        '`That\'s a strong choice. I think he\'s a really talented jungler. His ganks '
                                        'always seems to work. EDG Fofo is still my favorite player on this team '
                                        'though. I think you should focus on him too.`': 'end' # TODO
                                    },
                                    '[{fofo, chun lan, chunlan, mid, middle, midlaner}]': {
                                        '`That\'s a strong choice. I think he\'s one of the best midlaners in the world. His roam '
                                        'timings, laning, and mechanics are super strong. That\'s why he is my favorite player on this team '
                                        'I\'m glad we have similar interests.`': 'end' # TODO
                                    },
                                    '[{leave, hong chao, hongchao, bot, adc, bottom, botlaner}]': {
                                        '`That\'s an interesting choice. I think he\'s a really good adc. His team-fighting '
                                        'and laning is really strong. However, Meiko makes Leave seem a lot stronger in lane.`': 'end'  # TODO
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
                'best, probably because I\'m a part of it. What do you like about it?`' : {
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
                '`That\'s a strong choice. I think he\'s a really talented top laner. EDG Fofo '
                'is still my favorite player on this team though. I think you should focus on him too.`': 'end'  # TODO
            },
            '[{jiejie, li jie, lijie, jungle, jungler}]': {
                '`Awesome!. I think Jiejie\'s a really talented jungler. His ganks '
                'always seems to work. EDG Fofo is still my favorite player on this team '
                'though. I think you should focus on him too.`': 'end'  # TODO
            },
            '[{fofo, chun lan, chunlan, mid, middle, midlaner}]': {
                '`I think Fofo is the key to EDG\'s success. Both his roam '
                'timers and laning is strong. That\'s why he is my favorite player on this team '
                'I\'m glad we have similar interests.`': 'end'  # TODO
            },
            '[{leave, hong chao, hongchao, bot, adc, bottom, botlaner}]': {
                '`That\'s an interesting choice. I think he\'s a really good adc. His team-fighting '
                'and laning is really strong. However, Meiko makes Leave seem a lot stronger in lane.`': 'end'  # TODO
            },
            '[{meiko, tian ye, ye, sup, support}]': {
                '`Wow! He\'s one of my favorite players on EDG! What makes you think he\'s so good?'
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
                '`Are you sure that player currently plays for EDG? I only know players who play for them right now. Try another player.`': 'playerEDG'
            }
        }
    }

    keria = {
        'state': 'keria',
        '`Awesome! Tell me what you like about him.`': {
            'state': 'keria2',
            '[{playmaking, best, macro, mechanics, micro, macroplay, microplay, teamwork, champions, champion, good, talented, gifted, skilled}]': {
                'state':'keriaGameplay',
                '`Can you explain further?`': {
                    '[{no, not, dont, wont, cant}]': {
                        '`Well, I think that he\'s the best support in the world, and maybe even the best player in the world. Do you think he\'s stronger mechanically or with macro?`': {
                            '{<{stronger, better, best}, {mechanically, mechanics, mechanic}>, <{weaker, worse, worst, weak}, {macro, macroplay, strategy}>}': {
                                '`I also think his mechanical skill is stronger, but his macro and awareness is also world-class.`': {
                                    'state': 'keria3',
                                    '[{<{what, how}, {good, strong, way}>}]': {
                                        '`He always engages on winning fights. Each action he takes is precise and sets his team up for victory.`':'end'
                                    }
                                }
                            }
                        }
                    },
                    'error': {
                        '`For sure! I really believe that he\'s the best support, and maybe even the best player in the world. Do you think he\'s stronger mechanically or with macro?`': {
                            '{<{stronger, better, best}, {mechanically, mechanics, mechanic}>, <{weaker, worse, worst, weak}, {macro, macroplay, strategy}>}': {
                                '`I also think his strongest attribute is his mechanical skill. His macro and awareness is also world-class.`': {
                                    '[{<{what, how}, {good, strong, way}>}]': {
                                        '`He always engages on winning fights. Each action he takes is precise and sets his team up for victory.`': 'end'
                                    }
                                }
                            }
                        }
                    }
                }
            },
            '[{team, t1, skt}]': {
                '`Can you explain further?`': {
                    '[{no, not, dont, wont, cant}]': {
                        '`Well, I think that T1 is a really strong team. They always seem to win their games. What do you think makes them so strong?`': {
                            '[{faker, oner, zeus, gumayusi}]': {
                                '`They are definitely a key part to their success, but Keria seems like he\'s always the carry.`': {
                                    '<{why, what, how}, {him, he}>': {
                                        '`He\'s always around the map and makes it seem like it is a 10 v 5. If you need him he\'s there.`': {
                                            '[{no, not, false, wrong}]': {
                                                '`I guess that makes sense, but you should check his games out. He gets so many MVPs for a reason.`': 'end'
                                            },
                                            '[{yes, yeah, true, correct}]': {
                                                '`I\m glad you think the same way! I wish I could play with him. We would win every game!`': 'end'
                                            }
                                        }
                                    },
                                    '[{no, not, false, wrong}]': {
                                        '`Sorry, but I think Keria is the main reason why they\'re able to win so many matches.`': 'end'
                                    },
                                    '[{yes, yeah, true, correct}]': {
                                        '`I\m glad you think the same way!`': 'end'
                                    },

                                }
                            }
                        }
                    },
                    'error': {
                        '`T1 is definitely a fan-favorite team. They always seem to win their games. What makes them so strong?`': {
                            '[{faker, oner, zeus, gumayusi}]': {
                                '`They are definitely a key part to their success, but Keria seems like he\'s always the carry.`': {
                                    '[{why, what, how}, {him, he}]': {
                                        '`He\'s always around the map and makes it seem like it is a 10 v 5. If you need him he\'s there.`': {
                                            '[{nno, not, dont, false, incorrect, wrong}]': {
                                                '`I guess that makes sense, but you should check his games out. He gets so many MVPs for a reason.`': 'end'
                                            },
                                            '[{yes, yeah, true, correct, agree, yep}]': {
                                                '`I\m glad you think the same way! I wish I could play with him. We would win every game!`': 'end'
                                            },
                                            'error': {
                                                '`Gotcha. It was nice talking to you! I enjoyed our conversation a lot. See ya!`': 'end'
                                            }
                                        }
                                    },
                                    '[{no, not, dont, false, incorrect, wrong}]': {
                                        '`Well, I think Keria is the main reason why they\'re able to win so many matches.`': 'end'
                                    },
                                    '[{yes, yeah, true, correct, agree, yep}]': {
                                        '`I\m glad you think the same way!`': 'end'
                                    },
                                    'error': {
                                        '`Gotcha. It was nice talking to you! I enjoyed our conversation a lot. See ya!`': 'end'
                                    }
                                }
                            }
                        }
                    }
                }

            },
            '[{drx, dragon x, dragonx, previous team}]': {
                '`Although I don\'t know much about him on DRX, I know that he won Rookie of the Year in the LCK that '
                'year. Even from the start he was a really good player.`': 'end'
            },
            '[{fun, entertaining, fast, fastpaced, action, engaging}]': {
                '`Do you have any moments in particular?`': {
                    'error': {
                        '`I gotcha. To me, everytime he plays Thresh, it\'s a masterclass. You should check out any game that he plays that champ.`': 'end'
                    }
                }
            },
            'error': {
                '`I don\'t think I caught that. What do you like about him again?`': 'keria2'
            }
        }
    }
    return casual, edg, keria

#TODO connect these to convo.py