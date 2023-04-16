def laneInfo():
    laneInfo = {
        'state': 'laneInfo',
        '`There are 3 lanes in League of Legends: Top, Middle (or Mid), and Bottom (or Bot). There\'s 1 player in each lane, '
        'and the last 2 players fill the Support and Jungle roles. People choose their lane based on what they feel fits '
        'their playstyle best. In higher ranks, players will swap between roles from game to game, and across '
        'lanes within a single game. Which lane would you like to hear more about?`': {
            'state': 'laneInfoInner',
            '[top]': {
                'state': 'topLane',
                '`Top lane is often considered as the Lone Wolf. If you\'re a 1v1 enthusiast who wants to '
                'lean on your own skills and tactics to win the game by pouring tons of pressure on '
                'your foes, then it\'s a great choice for you!`': {
                    '[{enjoy, interesting, yes, yeah}]': {
                        'state': 'topArchetypes',
                        '`Great! Sounds like you are an 1v1 combat fans who want to overwhelm you foes with '
                        'superb skills. There are actually several archetypes for a typical top lane '
                        'champion, like tanks and duelists. Do you want to know more about them? `': {
                            'state': 'topArchsInner',
                            '[tank, tanks]': {
                                'state': 'laneInfoTank',
                                '`Tanks excel in shrugging off incoming damage and focus on disrupting their enemies, protecting their allies in the process. Popular tanks include Malphite, Ornn, and Sion. Would you like to hear about a different lane?`': {
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, mid, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[duelists]': 'laneInfoDuelist'
                                }
                            },
                            '[duelist, duelists]': {
                                'state': 'laneInfoDuelist',
                                '`Duelists are mobile melee champions that focus on damaging their opponents up close. Popular duelists include Fiora, Jax, and Gwen. Would you like to hear about a different lane?`': {
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, mid, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[tanks]': 'laneInfoTank'
                                }
                            },
                            'error': {
                                '`Sorry, I didn\'t catch that. Can you say that again for me?`': 'topArchsInner'
                            }
                        }

                    },
                    'error': {
                        '`Would you like to hear more about top lane champions?`': {
                            '[{yeah, yes, yup, yep, sure, ok}]': {
                                '`There are actually 2 main archetypes of top lane champs: tanks and duelists. Which would you like to hear about?`': 'topArchsInner'
                            },
                            '[{no, nah, nope, not really}]': {
                                '`Alright, do you want to hear about a different lane?`': {
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, mid, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition'
                                }
                            }
                        }
                    }
                }
            },
            '[{mid, middle}]': {
                'state': 'midLaneInfo',
                '`Mid lane is usually filled by fast, high damage champions. If you like playing quickly and '
                'dealing a lot of burst damage, then Mid would be a great choice for you!`': {
                    '[{enjoy, interesting, yes, yeah}]': {
                        'state': 'midArchetypes',
                        '`Nice, seems you like the sound of Mid lane! Most Mid lane champions are mages that '
                        'focus on ability power, but there are also assassins that focus more on physical attacks. '
                        'Do you want to know more about these champs?`': {
                            'state': 'midArchsInner',
                            '[{mage, mages, ability power}]': {
                                'state': 'laneInfoMage',
                                '`Mages are the spellcasters of the game, wielding powerful magic to obliterate their enemies. Popular mages include Lux, Veigar, and Annie. Would you like to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[{assassin, assassins}]': 'laneInfoAssassin'
                                }
                            },
                            '[{assassin, assassins}]': {
                                'state': 'laneInfoAssassin',
                                '`Assassins are like ninjas - fast, sneaky, and deadly! They excel at picking off high-value targets. Popular assassins include Zed, Katarina, and Fizz. Would you like to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[{mage, mages}]': 'laneInfoMage'
                                }
                            },
                            'error': {
                                '`Sorry, I didn\'t catch that. Can you say that again for me?`': 'midArchsInner'
                            }
                        }

                    },
                    'error': {
                        '`Would you like to hear more about mid lane champions?`': {
                            '[{yeah, yes, yup, yep, sure, ok}]': {
                                '`There are actually 2 main archetypes of mid lane champs: mages and assassins. Which would you like to hear about?`': 'midArchsInner'
                            },
                            '[{no, nah, nope, not really}]': {
                                '`Alright, do you want to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{jg, jungle}]': 'jungleInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, bot, support, or jungle?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition'
                                }
                            }
                        }
                    }
                }
            },
            '[{bot, bottom, adc, support, supp}]': {
                'state': 'botLaneInfo',
                '`Bot lane is the only lane with 2 champions from each team in it. The main damage dealer in Bot '
                'is also sometimes called the Attack Damage Carry, or ADC, since they\'re usually focused on '
                'doing a lot of damage. The second champion fills the Support role. They\'re focused on helping '
                'their team maintain vision of the map, as well as supporting the ADC in Bot lane and their '
                'team in team fights. Would you like to hear more about either of these roles?`': {
                    'state': 'botLaneInfoInner',
                    '[{adc}]': {
                        'state': 'laneInfoADC',
                        '`ADCs (also called Marksmen) are the sharpshooters of the game, dealing consistent damage from a distance. Popular ADCs include Ashe, Miss Fortune, and Jhin. Would you like to hear about a different lane?`': {
                            '[top]': 'topLaneInfo',
                            '[{mid, middle}]': 'midLaneInfo',
                            '[{jg, jungle}]': 'jungleInfo',
                            '[{yeah, yes, yup, yep, sure, ok}]': {
                                '`Which lane would you like to learn about, top, mid, or jungle?`': 'laneInfoInner'
                            },
                            '[{no, nah, nope, not really}]': 'laneInfoTransition',
                            '[{supp, support}]': 'laneInfoSupport'
                        }
                    },
                    '[{supp, support}]': {
                        'state': 'laneInfoSupport',
                        '`Supports are the unsung heroes of the game, providing utility, protection, and vision for their team. Popular supports include Soraka, Thresh, and Lulu. Would you like to hear about a different lane?`': {
                            '[top]': 'topLaneInfo',
                            '[{mid, middle}]': 'midLaneInfo',
                            '[{jg, jungle}]': 'jungleInfo',
                            '[{yeah, yes, yup, yep, sure, ok}]': {
                                '`Which lane would you like to learn about, top, mid, or jungle?`': 'laneInfoInner'
                            },
                            '[{no, nah, nope, not really}]': 'laneInfoTransition',
                            '[adc]': 'laneInfoADC'
                        }
                    },
                    'error': {
                        '`Sorry, I didn\'t catch that. Could you repeat that for me?`': 'botLaneInfoInner'
                    }
                }
            },
            '[{jungle, jg}]': {
                'state': 'jungleInfo',
                '`The Jungler is focused on defeating neutral monsters in the jungle to collect buffs for their '
                'team. They also roam between lanes to support their teammates in their individual lanes, which '
                'is also called ganking. If you like being active across the whole map, then Jungle would be a '
                'great choice for you!`': {
                    '[{enjoy, interesting, yes, yeah}]': {
                        'state': 'jgArchetypes',
                        '`Cool! Looks like you would be into Jungle! Jungle champs are usually divided in to early game '
                        'junglers and late game junglers. Do you want to learn more about either of these?`': {
                            'state': 'jgArchetypesInner',
                            '[early]': {
                                'state': 'laneInfoEarlyJG',
                                '`Early game junglers are good at skirmishes, so they try to start up fights before the game goes too long. Popular early game junglers include Rek\'sai, Rengar, and Elise. Would you like to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, mid, bot, or support?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[late]': 'laneInfoLateJG'
                                }
                            },
                            '[late]': {
                                'state': 'laneInfoLateJG',
                                '`Late game junglers aren\'t very good in fights at the start of the game, so they try to avoid fights and focus on farming neutral monsters. Popular late game junglers include Amumu, Zac, and Karthus. Would you like to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, mid, bot, or support?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition',
                                    '[early]': 'laneInfoEarlyJG'
                                }
                            },
                            'error': {
                                '`Sorry, I didn\'t catch that. Could you repeat that for me?`': 'jgArchetypesInner'
                            }
                        }

                    },
                    'error': {
                        '`Would you like to hear more about jungle champions?`': {
                            '[{yeah, yes, yup, yep, sure, ok}]': {
                                '`There are actually 2 main archetypes of jungle champs: early game and late game. Which would you like to hear about?`': 'jgArchetypesInner'
                            },
                            '[{no, nah, nope, not really}]': {
                                '`Alright, do you want to hear about a different lane?`': {
                                    '[top]': 'topLaneInfo',
                                    '[{mid, middle}]': 'midLaneInfo',
                                    '[{bot, bottom, supp, support}]': 'botLaneInfo',
                                    '[{yeah, yes, yup, yep, sure, ok}]': {
                                        '`Which lane would you like to learn about, top, mid, bot, or support?`': 'laneInfoInner'
                                    },
                                    '[{no, nah, nope, not really}]': 'laneInfoTransition'
                                }
                            }
                        }
                    }
                }
            },
            '[{dont, no, none, fine}]': {
                'state': 'laneInfoTransition',
                '`Ok, what would you like to know more about: the different types of champions, in-game objectives, or the map?`': {
                    '[{champions, types}]': 'IntroduceChampions',
                    '[{objectives, in-game}]': 'IntroduceObjectives',
                    '[{roles, positions}]': 'IntroduceRoles',
                    '[{map, layout}]': 'IntroduceMap',
                    '[{no, none, nothing, fine}]': 'EndIntroduceGame',
                }
            },
            'error': {
                '`Sorry, I didn\'t catch that. Which lane do you want to learn about?`': 'laneInfoInner'
            }
        }
    }
    return laneInfo
