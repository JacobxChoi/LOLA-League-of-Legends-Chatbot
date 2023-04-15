def advanced():
    advanced = { #user has just mentioned that they actively watch the game mentioned in casual.
        'state': 'advanced',
        '`What did you think about the game?`': { #TODO: HANDLE CASES LIKE "I LIKED IT"
            '{good, competitive, close, fun, well}': {
                '#CLOSE `Who do you think performed the best?`': {
                    # Should reply with if the game was close or not
                    'state': 'perform',
                    '[$BEST_PLAYER = #ONT(teams)]': {
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
                                    '[#ONT(teams)]': {
                                        '`That\'s debatable... in what way?`',
                                        '`I guess that could be true...can you explain?`',
                                        '`No way you think that! Prove it!`'
                                    }
                                }

                            },
                            'error': {
                                '`Can you say that again, I didn\'t catch that...`': 'agreement'
                            }
                        },
                        '{agree, yes, yeah, sure}': {
                            '`Is there another player that you thought performed well this game?`': {
                                '[$GOOD_PLAYER=#ONT(teams)]': {
                                    '`What made him particularly stand out?`': {
                                        '{laning, fighting, objective control, vision control, roaming, itemization, wave management}': 'skills',
                                        'error': {
                                            '`I\'m not so sure about that... What\'s another skill that you think he excelled at?`': 'skills'
                                        }
                                    }
                                }
                            },

                    }

                }
            },
            '{boring, bad, #LEM(stomp), [not close]}': {
                '#CLOSE2` Who do you think was the winning factor for the game? I personally think it was` #BESTPLAYER': { #Should reply with if the game was close or not
                    '[$BEST_PLAYER=#ONT(teams)]': {

                    }
                }
            },
            'error': {
                '`I\'m not sure if I understood.`': 'advanced'
            }
            }

        },
        '#GATE `Do you think anyone showed a lot of improvement over their last game?`': {
            'score': 0.9,
            '[$MOST_IMPROVED=#ONT(teams)]': {
                '`What did they do to improve the most?`': {

                }
            },
            '{not, no, [not that i know of]}': {
                '`Hmm...`'
            }
        },
        '#GATE `Do you think anyone has been performing worse than usual?`': {
            'score': 0.8,
            '[$UNDERPERFORMING=#ONT(teams)]': {
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