from .buildInfo import buildInfo
from .champInfo import championInfo
from .laneInfo import laneInfo

buildInfo = buildInfo()
champInfo = championInfo()
laneInfo = laneInfo()


def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeagueEsports',
        '`That\'s fine. Have you ever played League of Legends?.`': {
            '[{yes, yeah}]': {
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
            '[{no, not, dont, never}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                '#GATE `What\'s your favorite game?`': {
                    'score': '1',
                    # TODO: catch circumstance if the user do not have favorite game
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME': 'transit'
                    },
                    'error': {
                        '` (ﾟ∀。) Sounds like an interesting game, I\'ll definitely try it some day!`': 'transit',
                    }
                },

                '#GATE `Why are you interested in League esports?`': {
                    'state': 'interest',
                    'score': '0.8',
                    '[{friend, friends, social, community}]': {
                        '`Yeah, a shared interest in game connects friends together. What do you typically do with friends in your free time?`': {
                            '[#ACTIVITY_WITH_FRIENDS]': {
                                '`Definitely, I wish I would have chance to` #GET_ACTIVITY_FRIEND ` with my friends too`': 'transit'
                            },
                        }
                    },
                    '[{fun,challenging,exciting}]': {
                        '`For sure! After all, the adrenaline rush after watching an exciting matches is true. Do you enjoy the watching other sports events as well?`': {
                            '[#SportEvents]': {

                            }
                        }
                    },

                    '[{waste, time}]': {
                        '`Ha, Sounds like you have fallen into the trap of modernism. I guess there are better ways to use your time.`': 'transit'
                    },

                    '[$FAV_PLAYER=#ONT(leagues)]': {
                        '#IF($FAV_PLAYER = jojopyun) `Agree! Jojopyun is my favorite player too.`': 'transit',
                        '`I like` $FAV_PLAYER `too`': 'transit',
                        'error': 'loveLeague',
                    },
                    '[{not, not really, no, dont}]': {
                        '`Oh ok, so I guess you just want to get some info on the subject.`': 'transit'
                    },
                    '[{bye,exit}]': {
                        'state': 'quit',
                        '`Adieu, hope to see you again.`': 'end'
                    },
                    'error': {
                        'state': 'loveLeague',
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                },

                '`Do you want to know more about the League of Legends? I can give you a brief introduction of the '
                'game goal, champion selection, and some advice for improving in-game skills`': {
                    'state': 'IntroduceLeague',
                    'score': '0.5',

                    '[{sure, yes}]': {
                        '#GATE `Great! Do you know how to win a league of legends game?`': {
                            'state': 'Directed_Questions',

                            '[{nexus, base, tower}]': {
                                'state': 'DestroyNexus',
                                'score': '1.0',
                                '`Exactly! League of legends or LOL is a 5 players vs. 5 players MOBA game, where teammates cooperate together to destroy other team\'s base and of course, there are many hindrance on the way toward final goal `': {
                                    '[{what},{base}]': {
                                        '`Base is like the \'headquaters\' of a team where waves of minions enter the battlefields. The game ends if you destroy the nexus on the base of the other team.`': {
                                            '[{minion， minions}]': {
                                                'score': '1.0',
                                                '`Hmm, If the champions users control are heroes that can dominate the victory or defeat of the game, minions are the front-line fighters that can rush against the defense of the foe and take the damage from the turret on behalf of the player. Otherwise, players cannot enter the base of the other team `': {

                                                    '[{minion}, {essential, key, important}]': {
                                                        'state': 'minion',
                                                        'Yeah, the waves of minions that can bear the boat of the victory is the same that swallows it. So, it\'s important to have a sophisticated control of the minions in order to win the game': {
                                                            '[{explain,know, more},{control}]': {
                                                                'state': 'toMinionWaveControl',
                                                                'The skill is really learned and honed with thinking in actual practice, but for sure I can give you some hint if you want to know ': {
                                                                    '[#AgreementChecker]': {
                                                                        '#IF(#POSITIVE_AGREEMENT) `Wow, it\'s great you have interest in it. I can give you the experience I summarized from playing the game. More is for you to explore`': 'MinionwaveControl', # TODO complete the branch of the dialogue
                                                                        '#IF(#NEGATIVE_AGREEMENT) `That\'s alright. I guess to find the interest for a game is more important for a beginner rather than get overwhelmed by those concerns. What else do you want to know`': 'IntroduceLeague',
                                                                        'error': {
                                                                            '`Forgive me for my inability to understand you, but do you know the goal of league of legends?`': 'Directed_Questions'
                                                                        }
                                                                    }
                                                                }
                                                            },

                                                            '[{hard, complicated}]': {
                                                                '`Don\'t be overwhelmed by this, with practice, you\'ll definitely become more and more experienced in this ! Do you have other questions ？`': 'IntroduceLeague',
                                                            },

                                                            '[{interesting, challenging}]': 'toMinionWaveControl',

                                                            'error': {
                                                                ' (́◉◞౪◟◉‵) Pardon my absent-mindedness just then. Could you explain it ?': 'minion'
                                                            }
                                                        }

                                                    }

                                                }

                                            },

                                            '[turret, turrets]': {
                                                'state': 'turrets',
                                                '`Turrets can give high damage if you hastily intrude into its range when your minions are absent. It\'s one of the main obstacle on your way to destroy the nexus`': {
                                                    '[{protect}, {own}]': {
                                                        '`You really have the talents! Turrets are \'strategic weapons\' that we should protect to protect our base from being attacking`': {

                                                        }
                                                    },

                                                    '[{not, dont},{understand, sure, get}]': {
                                                        'score': '0.7',
                                                        '`You can think those turrets as guardians that protect your base form enemy attacks. So you really want to try hard to protect your own turrets while destoying the enemy turrents with your minions`': {
                                                            '[{how},{protect}]':{
                                                                '`Good question! Turrets will only receive a little damage when the enemy minions are not in its range. In this case, you really want to try hard to keep enemy minions away from your turrets`':{

                                                                }
                                                            },
                                                            '[{understand, get}]': {
                                                                'score': '0.5',
                                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'

                                                            },

                                                            'error': {
                                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                            }
                                                        }

                                                    },

                                                    '[{understand, get}]': {
                                                        'score': '0.5',
                                                        '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                    },

                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry for missing you, could you explain more for your request ?`': 'DestroyNexus'
                                                    }

                                                }

                                            },


                                            '[{not, dont},{understand, sure, get}]': {
                                                'score': '0.7',
                                                # TODO: COMMONITY with the game user select

                                            },

                                            '[{understand, get}]': {
                                                'state': 'understandLeague',
                                                'score': '0.5',
                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'

                                            },

                                            'error': {
                                                '`(≧∀≦)ゞ I\'m really sorry for missing you, could you explain more for your request ?`': 'DestroyNexus'
                                            }
                                        }
                                    },
                                    '[{played},{MOBA}]': {
                                        '`Wow, which one did you play? Have you played DOTA 2 or Vain Glory ?`': {
                                            '[DOTA]': { # TODO: Expand later
                                                'score': '1.0',
                                                '`Then, I guess you\'ll master league of legends quicker as DOTA 2 shares the similar core structure with LoL despite a way more complex systems `': {
                                                    'state': 'compareWithDOTA',
                                                    '[different, difference]': {
                                                        '`Hmm, in league of legends, you can not kill your own minions and no courier units are there. Also, each game takes less time, making it possibly more cater to the high-paced life.`': {
                                                            '[{understand, get, see}]': {
                                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                            },
                                                            'error': {
                                                                '`(´・ω・`) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                            }
                                                        }
                                                    },
                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry for missing you, could you explain more for your request ?`': 'compareWithDOTA'
                                                    }
                                                }
                                            },
                                            '[Vain Glory]': { # TODO: Expand later
                                                'score': '1.0',
                                                '`Then, I guess you\'ll enter league of legends more smoothly as the core structure is similar`': {
                                                    'state': 'compareWithVG',
                                                    '[different, difference]': {
                                                        '`Different from vain glory which is designed more for ios and android and support for touchscreen control, lol is mainly on pc. And there are 3 lanes instead of 1 lane in lol`': {
                                                            '[{understand, get, see}]': {
                                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                            },
                                                            'error': {
                                                                '`(´・ω・`) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                                            }
                                                        }

                                                    },
                                                    'error': {
                                                        '`(≧∀≦)ゞ I\'m really sorry for missing you, could you explain more for your request ?`': 'compareWithVG'
                                                    }
                                                }

                                            },

                                            '[{played, play, playing}]': {
                                                'score': '0.5',

                                                # TODO: add this later


                                            },

                                            'error': {
                                                '`(ゝ∀･) That\'s great! Do you have other questions ?`': 'IntroduceLeague'
                                            }


                                        }

                                    },
                                    '[{what},{MOBA}]': {
                                        '`MOBA is the synonym of Multi-player Online Battle Arena, in league of legends, 5 players on each team are working together in the battle fields with the shared goal to destroy the nexus of the other team. `': {

                                            '[{arena, battlefield}]': 'mapInfo', #TODO connect to mapInfos


                                            '[{understand, get}]': {
                                                '`ξ( ✿＞◡❛) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                            },
                                            'error': {
                                                '`(´・ω・`) , Do you have other questions related to league of legends ?`': 'IntroduceLeague'
                                            }


                                        }

                                    },
                                    '[hindrance]': 'turrets',

                                    '[{how},{destroy}]': {

                                        # TODO: add this later


                                    },

                                    'error': {
                                        '`(≧∀≦)ゞ I\'m really sorry for missing you, could you explain more for your request ?`': 'Directed_Questions',
                                    }

                                }

                            },
                            '[#AgreementChecker]': {
                                'score': '0.5',
                                '#IF(#POSITIVE_AGREEMENT) `Wow! Could you explain it to me. I guess different people understand it in different ways`': 'IntroduceLeague',
                                '#IF(#NEGATIVE_AGREEMENT)': 'GameGoal',
                                'error': {
                                    '`Forgive me for my inability to understand you, but do you know the goal of league of legends?`': 'Directed_Questions'
                                }

                            },

                        }
                    },

                    '[{goal, win}]': 'DestroyNexus',
                    '[{#LEM(improve), enhance}]': 'howToImprove',
                    '[{champion}]': 'champInfo',
                    '[{role,lane}]': 'roleInfo',
                    '[{map}]': 'mapInfo',
                    '[{item}]': 'items',

                    'error': {
                        '`Sorry, I didn\'t catch that, could you say it again?`': 'IntroduceLeague'
                    }
                },

            },

            'error': {
                '`Sorry, I didn\'t catch that, could you say it again?`': 'transit'
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
