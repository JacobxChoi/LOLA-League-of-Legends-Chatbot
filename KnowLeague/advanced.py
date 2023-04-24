def advanced():
    advanced = { #user has just mentioned that they actively watch the game mentioned in casual.
        'state': 'advanced',
        '`What did you think about the game?`': { #TODO: HANDLE CASES LIKE "I LIKED IT"
            'state':'thoughtsGame',
            '[{good, competitive, close, fun, well, liked}]': {
                '`Who do you think performed the best?`': {
                    # Should reply with if the game was close or not
                    'state': 'perform',
                    '[$BEST_PLAYER = #ONT(leagues)]': {
                        '#IF(#BESTPLAYER = $BEST_PLAYER)': {
                            '`I agree! I think that` $BEST_PLAYER `was the most efficient player this game. What do you think made his performance so strong?`': {
                                'state': 'choose_skills',
                                '$SKILLS = {laning, fighting, objective control, vision control, roaming, itemization, wave management}': 'skills'
                            }
                        },
                        '`I see... I think` #BESTPLAYER` performed the best this game. I think he really excelled in` #BESTSKILLS`. What do you think?`': {
                            'state': 'agreement',
                            'score': 0.9,
                            '{agree, yes, yeah, sure}': {
                                '`Nice! Is there another player in this game you want to talk about?`': 'perform'
                            },
                            '{disagree, no, not, don\'t}': {
                                '#GATE `Darn, that\'s unfortunate. Is there another skill you think` $BEST_PLAYER `did well in?`': 'choose_skills',
                                '#GATE `Then who do you think outperformed` $BEST_PLAYER `?`': {
                                    'state': 'outperform',
                                    '[#ONT(teams)]': {
                                        '`That\'s debatable... in what way?`': {
                                            'error': {
                                                '`I see. I still think that` $BEST_PLAYER`was the most influential this game.': 'end'
                                            }
                                        },
                                        '`I guess that could be true...can you explain?`': {
                                            'error': {
                                                '`I gotcha. I still think that` $BEST_PLAYER`was the strongest player this game.`': 'end'
                                            }
                                        },
                                        '`No way you think that! Prove it!`': {
                                            'error': {
                                                '`For sure, but I still think that` $BEST_PLAYER`was the best performer this game.`': 'end'
                                            }
                                        },
                                    },
                                    'error': {
                                        '`I\'m not sure if that player played in this game. Maybe you misspelled their name.`': 'outperform'
                                    }
                                }
                            },
                            '{agree, yes, yeah, sure}': {
                                '`Is there another player that you thought performed well this game?`': {
                                    '[$GOOD_PLAYER=#ONT(teams)]': {
                                        '`What made him particularly stand out?`': {
                                            '{laning, fighting, objective control, vision control, roaming, itemization, wave management}': 'skills',
                                            'error': {
                                                '`I\'m not so sure about that... Maybe there\'s another skill that you think he excelled at?`': 'skills'
                                            }
                                        }
                                    },
                                    '[no, not, dont, didnt, cant, bad]': {
                                        '`That makes sense. Who do you think performed the worst then?`': 'worst'
                                    },
                                    'error': {
                                        '`I see where you\'re coming from. Is there a player you think performed poorly?`': 'worst'
                                    }
                                }
                            },
                            'error': {
                                '`Can you reword that, I didn\'t quite catch that...`': 'agreement'
                            }
                        }
                    }
                }
            },
            '[{boring, bad, #LEM(stomp), [not close]}]': {
                '#CLOSE2` Who do you think was the winning factor for the game?`': { #Should reply with if the game was close or not
                    '[$BEST_PLAYER=#ONT(teams)]': {
                        '#IF($BEST_PLAYER = #BESTPLAYER)': {
                            'score': 1.0,
                            '`I thought so too!`': {

                            }
                        },
                        'score': 0.9,
                        '`In what way?`': {
                            'error': {
                                '`Ohhhh, that makes a lot of sense. I personally think that` #BESTPLAYER `was the most influential. What do you think about` #BESTPLAYER`?`': {
                                    'error': {
                                        '`For sure. It was nice talking to you about LoL. I hope that we can talk again soon!`': 'end'
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'error': {
                '`I\'m not sure if I understood. Did you think the game was good, or bad?`': 'thoughtsGame'
                # TODO: I guess error state is useful there when the user give other response than "good"...
            },

        },
        '#GATE `Do you think anyone showed a lot of improvement over their last game?`': {
            'score': 0.9,
            '[$MOST_IMPROVED=#ONT(leagues)]': {
                '`What did they do to improve the most?`': {

                }
            },
            '{not, no, [not that i know of]}': {
                '`Hmm...`'
            }
        },
        '#GATE `Do you think anyone has been performing worse than usual?`': {
            'score': 0.8,
            'state': 'worst',
            '[$UNDERPERFORMING=#ONT(leagues)]': {
                '`What have they been struggling with the most lately?`': {
                    '[$WORSE_SKILL = {laning, fighting, objective control, vision control, roaming, itemization, wave management}]': {
                        '`I agree.`$UNDERPERFORMING `has been lacking in that department.`': 'end'
                    }
                }
            }
        }
    }
    return advanced

#MACRO CLOSE looks at the change in gold leads based on the gold graph
#MACRO EFFICIENCY