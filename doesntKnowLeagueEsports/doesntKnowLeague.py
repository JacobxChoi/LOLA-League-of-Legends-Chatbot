from .buildInfo import buildInfo
from .champInfo import championInfo
from .laneInfo import laneInfo

buildInfo = buildInfo()
champInfo = championInfo()
laneInfo = laneInfo()


def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeagueEsports',
        '`That\'s fine. Have you ever played League of Legends?`': {
            'state': 'playedLOL',
            '[{yes, yeah, yup}]': {
                'state': 'familiarity',
                '`Do you have a favorite champion?`': {
                    '#UserChamp': {
                        # ontology for favorite champion. Does not unfortunately handle cases where user has no favorite champion
                        '$FAV_CHAMP `is fun to play!` $PLAYER_RECOMMEND`plays them as well.`': 'end'
                    },
                    '[{no, not really, not}]': {
                        '`All good. My favorite champion is Irelia. I like playing aggressively and getting kills, so I find playing Irelia pretty fun.`': 'end'
                    },
                    'error': 'end'
                }
            },
            '[{no, nope, not, dont, never, barely, little bit}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                '#GATE `What\'s your favorite game?`': {
                    'score': '1',
                    # TODO: catch circumstance if the user do not have favorite game
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME': 'transit'
                    },
                    'error': {
                        '` (ﾟ∀。) Sounds like an interesting game, I\'ll definitely try it some time!`': 'transit',
                    }
                },

                '#GATE `Why are you interested in League esports?`': {
                    'state': 'interest',
                    'score': '0.8',
                    '[{friend, friends, social, community}]': {
                        '`Yeah, a shared interest in games connects friends together. What do you typically do with friends in your free time?`': {
                            '[#ACTIVITY_WITH_FRIENDS]': {
                                '`Definitely, I wish I would have the chance to` #GET_ACTIVITY_FRIEND `with my friends too.`': 'transit'
                            },
                        }
                    },
                    '[{fun, challenging, exciting}]': {
                        '`For sure! After all, the adrenaline rush after watching an exciting matches is true. Do you enjoy the watching other sports events as well?`': {
                            '[#SportEvents]': {

                            }
                        }
                    },

                    '[{waste, time}]': {
                        '`Ha, sounds like you\'ve fallen into the trap of modernism. I guess there are better ways to use your time.`': 'transit'
                    },

                    '[$FAV_PLAYER=#ONT(leagues)]': {
                        '#IF($FAV_PLAYER = jojopyun) `Agree! Jojopyun is my favorite player too.`': 'transit',
                        '`I like` $FAV_PLAYER `too`': 'transit',
                        'error': 'loveLeague',
                    },
                    '[{not, not really, no, dont}]': {
                        '`Oh ok, so I guess you just want to get some info on the subject.`': 'transit'
                    },
                    '[{bye, exit}]': {
                        'state': 'quit',
                        '`Adieu, hope to see you again.`': 'end'
                    },
                    'error': {
                        'state': 'loveLeague',
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                },

                '`Do you want to know more about League of Legends? I can give you a brief introduction of the '
                'game goal, champion selection, and some advice for improving in-game skills.`': {
                    'state': 'IntroduceLeague',
                    'score': '0.5',

                    '[{sure, yes}]': {
                        '#GATE `Great! Do you know how to win a League of legends game?`': {
                            'state': 'Directed_Questions',

                            '[{nexus, base, turrets}]': {
                                'state': 'DestroyNexus',
                                'score': '1.0',
                                '`Exactly! League of legends or LoL is a 5 versus 5 MOBA game, where teammates cooperate together to destroy the other team\'s base and, of course, there are many obstacles on the way to final goal.`': {
                                    'state': 'Base',
                                    '[{what}, {base, nexus}]': {
                                        '`The base is like the \'headquaters\' of a team where waves of minions enter the battlefield from. The game ends if you destroy the nexus on the base of the other team, but you can\'t do this without relying on your minions.`': {
                                            '[{minion, minions}]': {
                                                'score': '1.0',
                                                'state': 'Minions',
                                                '`Where champions are the heroes that individual players control, minions are non-controlled front-line fighters that can rush against the defense of the foe and take the damage from the turret on behalf of the player. Without them, players wouldn\'t be able to enter the base of the other team.`': {
                                                    'state': 'minion',
                                                    '[{minion, minions, they}, {essential, key, important}]': {
                                                        'state': 'MinionImportant',
                                                        '`Yeah, the waves of minions that can bear the boat of the victory is the same that swallows it. So, it\'s important to have sophisticated control of the minions in order to win the game.`': {
                                                            '[{explain, know, more},{control}]': {
                                                                'state': 'toMinionWaveControl',
                                                                '`The skill is really learned and honed with thinking in actual practice, but for sure I can give you some hints if you\'d like to know.`': {
                                                                    '[#AgreementChecker]': {
                                                                        '#IF(#POSITIVE_AGREEMENT) `Wow, it\'s great you have interest in it. I can give you the experience I summarized from playing the game. More is for you to explore`': 'MinionwaveControl',
                                                                        # TODO complete the branch of the dialogue
                                                                        '#IF(#NEGATIVE_AGREEMENT) `That\'s alright. I guess it\'s more important for a beginner to find an interest for the game rather than getting overwhelmed with details. What else do you want to know`': 'IntroduceLeague',
                                                                        'error': {
                                                                            '`Forgive me for my inability to understand you, but do you know the goal of League of Legends?`': 'Directed_Questions'
                                                                        }
                                                                    }
                                                                }
                                                            },

                                                            '[{hard, complicated}]': {
                                                                '`Don\'t be overwhelmed by this, with practice, you\'ll definitely become more and more experienced in this! Do you have any other questions?`': 'IntroduceLeague',
                                                            },

                                                            '[{interesting, challenging}]': 'toMinionWaveControl',

                                                            'error': {
                                                                '`(◉◞౪◟◉) Pardon my absent-mindedness just then. Could you say that again?': 'MinionImportant'
                                                            }
                                                        }

                                                    },

                                                    '[{understand, get}]': {
                                                        '`ξ( ✿＞◡❛)`': 'MinionImportant'
                                                    },

                                                    # TODO: add more options here

                                                    'error': {
                                                        '`(◉◞౪◟◉) Pardon my absent-mindedness just then. Could you say that again?': 'minion'
                                                    }

                                                }

                                            },

                                            '[turret, turrets, tower]': {
                                                'state': 'turrets',
                                                '`Turrets, also called towers, can deal high damage if you hastily enter into their range without your minions by you. Turrets are the main obstacles on your way to destroy the nexus.`': {
                                                    '[{protect}, {own}]': {
                                                        '`You really have the talents! Turrets are \'strategic weapons\' that we need to protect in order to protect our base from being attacked.`': {

                                                        }
                                                    },

                                                    '[{not, dont}, {understand, sure, get}]': {
                                                        'score': '0.7',
                                                        '`You can think those turrets as guardians that protect your base from enemy attacks, so you really want to try hard to protect your own turrets while destroying the enemy turrets alongside your minions.`': {
                                                            '[{how}, {protect}]': {
                                                                '`Good question! Turrets take the most damage from enemy champions, so you want to try to avoid leaving your turrets alone with enemy champions, especially while they have minions in your lane.`': {

                                                                }
                                                            },
                                                            '[{understand, get}]': {
                                                                'score': '0.5',
                                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'

                                                            },

                                                            'error': {
                                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                            }
                                                        }

                                                    },

                                                    '[{understand, get}]': {
                                                        'score': '0.5',
                                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    },

                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry for missing that, could you explain what you\'re asking again?`': 'Base'
                                                    }

                                                }

                                            },

                                            '[{not, dont},{understand, sure, get}]': {
                                                'score': '0.7',
                                                '`#GameGoalAnalogy`': {
                                                    '[{resources, resource}]': {
                                                        '`Enemy champions, neutral monsters, minions, turrets. You gain experience and gold from these, which allows you to build up weapons and armor.`': {
                                                            '[{build, weapon, armor}]': 'buildInfo',
                                                            '[{minions, minion}]': 'Minions',
                                                            '[{turrets}]': 'turrets',
                                                            '[{monsters}]': {
                                                                'state': 'neutralMonsters',
                                                                '`There are many different types of neutral monsters distributed symmetrically across the map. You can gain gold, experience, and buffs from defeating them.`': {
                                                                    'state': 'MonstersInfo',
                                                                    '[{type, different}]': {
                                                                        '`Great, I can guide you across the Summoner\'s Rift to see the ecology of the monsters. You can always stop me for further information and feel free to take off the safari vehicles. We will leave you around the monsters (=^-ω-^=). Are you prepared to set out on the journey?`': {
                                                                            'state': 'MonsterTrip',
                                                                            '[{ecology}]': {
                                                                                'score': '1.0',
                                                                                '`I\'m just kidding. So, are you ready to set out on the zoo trip?`': 'MonsterTrip'
                                                                            },
                                                                            '[#AgreementChecker]': {
                                                                                'score': '0.5',
                                                                                '#IF(#POSITIVE_AGREEMENT) `It\'s my great pleasure to guide you through this investigative trip of the monsters. Our first destination is the blue sentinels, which guard the power of crests of Insight.`': {
                                                                                    'state': 'MonsterFirstGlance',



                                                                                },
                                                                                '#IF(#NEGATIVE_AGREEMENT)': 'GameGoal',
                                                                                'error': {
                                                                                    '`Σ(°Д°) A monster is right in front of us. Do you see the large, blue, golem-like creature with a blue crystalline body? That\'s a blue sentinel. Together with its 2 minions, they are fearsome monsters, but tempting treasures for greedy, novice hunters.`': 'MonsterFirstGlance'
                                                                                }

                                                                            },

                                                                            '[{other}]': {
                                                                                'score': '0.7',
                                                                                '`Well, what other questions do you have about League of Legends and League esports?`': 'IntroduceLeague',

                                                                            },

                                                                            'error': {
                                                                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Are prepared for the trip or do you want to switch to other questions?`': 'MonsterTypes',
                                                                            }
                                                                        }

                                                                    },

                                                                    'error': {
                                                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'neutralMonsters',
                                                                    }

                                                                }
                                                            },
                                                            'error': {
                                                                '`༼ つ◕_◕ ༽つ Do you have other questions about League?`': 'IntroduceLeague',
                                                            }
                                                        }

                                                    },

                                                    '[{what}, {weapon, defense}]': {
                                                        'state': 'buildInfo',
                                                        '`Appropriate builds include weapons, clothes... , that you can purchase in your base. These can greatly enhance your power and help you gain an edge in combat. For a beginner, you can just follow the recommended items that automatically show when you open the shop.`': {
                                                            '[{purchase, buy}]': {

                                                            },

                                                            'error': {
                                                                '`(≧∀≦)ゞ My apologies, could you explain what you\'re asking a little more please? `': 'IntroduceLeague',

                                                            }
                                                        }

                                                    },

                                                    '[{competitive}]': {

                                                    },

                                                    '[{why}, {brain}]': {
                                                        '`A game is like a dream, where players are forced into sets of absurd rules, and they\'re happy with it. But that\'s off-topic. Do you have other questions about the game goal?`': 'Directed_Questions',
                                                    },

                                                    '[{understand, get}]': 'understandLeague',
                                                    'error': {
                                                        '`(*\'ω\')人(\'ω\'*) Cool! do you have other questions about the game?`': 'IntroduceLeague'
                                                    }

                                                }

                                            },

                                            '[{understand, get}]': {
                                                'state': 'understandLeague',
                                                'score': '0.5',
                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'

                                            },

                                            'error': {
                                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'DestroyNexus'
                                            }
                                        }
                                    },
                                    '[{played}, {moba}]': {
                                        '`Wow, which one did you play? Have you played DOTA 2 or Vain Glory ?`': {
                                            '[dota]': {  # TODO: Expand later
                                                'score': '1.0',
                                                '`Then I guess you\'ll get a handle on League of Legends quicker, since DOTA shares a lot of core elements with LoL despite some of its more complex systems.`': {
                                                    'state': 'compareWithDOTA',
                                                    '[different, difference]': {
                                                        '`Well, in League of Legends, you can\'t kill your own minions and there aren\'t any courier units. Also, each game takes less time, making it possibly more catered to a fast-paced life.`': {
                                                            '[{understand, get, see}]': {
                                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                            },
                                                            'error': {
                                                                '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                            }
                                                        }
                                                    },
                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'compareWithDOTA'
                                                    }
                                                }
                                            },
                                            '[vainglory]': {  # TODO: Expand later
                                                'score': '1.0',
                                                '`Then I guess you\'ll be able to transition to League of Legends more smoothly, since the core elements are similar between LoL and Vainglory.`': {
                                                    'state': 'compareWithVG',
                                                    '[different, difference]': {
                                                        '`The key difference is that Vainglory is designed more for iOS and Android, and it supports touchscreen control. LoL is mainly on PC, so the controls and menus are geared around mouse and keyboard input. Also, there are 3 lanes on the map in LoL instead of just 1.`': {
                                                            '[{understand, get, see}]': {
                                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                            },
                                                            'error': {
                                                                '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                            }
                                                        }
                                                    },
                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'compareWithVG'
                                                    }
                                                }
                                            },
                                            '[{played, play, playing}]': {
                                                'score': '0.5',
                                                '`Great! MOBA games all share similar core design, so you\'ll definitely master LoL faster than most people! Do you have any other questions?`': 'IntroduceLeague'
                                            },
                                            'error': {
                                                '`(ゝ∀･) That\'s great! Do you have any other questions?`': 'IntroduceLeague'
                                            }
                                        }
                                    },
                                    '[{what},{moba}]': {
                                        '`MOBA is an acronym for Multiplayer Online Battle Arena. In League of Legends, for example, 5 players on each team are working together in the battlefield of Summoner\'s Rift with the shared goal to destroy the other team\'s Nexus.`': {

                                            '[{arena, battlefield}]': 'mapInfo',  # TODO connect to mapInfos

                                            '[{understand, get}]': {
                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                            },
                                            'error': {
                                                '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                            }

                                        }

                                    },
                                    '[hindrance]': 'turrets',

                                    '[{how}, {destroy}]': {

                                        '`There are no way for you destroy the base unless you destroy all turrets in a lane and two guardian towers in front of the nexus to destroy the base with help from your minions.`': {
                                            '[{tower, turrets}]': 'turrets',
                                            '[{minions}]': 'Minions',
                                            '[{lot, many}]': {
                                                '`I know it sounds like a hard mission, but when you take to the battlefield, enemy turrets will be demolished like piles of sand in the wind.`': 'end'
                                            },
                                            '[{lane}]': 'laneInfo',
                                            'error': {
                                                '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                            }
                                        }

                                    },

                                    'error': {
                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'Base',
                                    }
                                }
                            },
                            '[#AgreementChecker]': {
                                'score': '0.5',
                                '#IF(#POSITIVE_AGREEMENT) `Wow! Could you explain it to me? I guess different people understand it in different ways.`': 'IntroduceLeague',
                                '#IF(#NEGATIVE_AGREEMENT)': 'GameGoal',
                                'error': {
                                    '`Forgive me for my inability to understand you, but do you know the goal of a game of League of Legends?`': 'Directed_Questions'
                                }
                            },

                            'error': {
                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'Directed_Questions',
                            }
                        }
                    },

                    '[{goal, win}]': 'DestroyNexus',
                    '[{champion}]': 'champInfo',
                    '[{role,lane}]': 'laneInfo',
                    '[{map}]': 'mapInfo',
                    '[{item}]': 'items',
                    #TODO: HANDLE CASE WHERE USER SAYS NO
                    'error': {
                        '`Sorry, I didn\'t catch that, could you say it again?`': 'IntroduceLeague'
                    }
                },

            },

            'error': {
                '`Sorry, I didn\'t catch that, could you say it again? ξ( ✿＞◡❛)`': 'playedLOL'
            },

        },

    }

    items = {
        'state': 'items',
        '`Items are intimidating at first glance, but they\'re actually pretty simple. Items are purchased from the '
        'store in your base, and they provide positive effects to you. Most items provide stat bonuses, but some grant '
        'a passive ability, and some are consumables that have some effect when used. Do you want me to explain any '
        'of that in more depth?`': {
            '[{how}, {buy}, {money, gold}]': {
                '`Items are bought with gold, which you passively acquire throughout the game. You can also get more '
                'gold by defeating minions, enemy champs, or jungle monsters, or by destroying enemy structures. Any '
                'other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceLeague'
                    },
                    'error': 'items'
                }
            }
        }
        # TODO: add info about items
    }

    base = {
        'state': 'base',
        '`Each team has their base at opposite corners of the map. The base is where players respawn after getting '
        'killed, as well as where they can heal their HP and buy items. The nexus is in the center of the base, '
        'protected by 2 turrets which do massive damage to champions in their range. Once one team destroys their '
        'opponents nexus, they win the game.`': 'end'
    }

    return doesntKnowLeague, items, base, laneInfo,
