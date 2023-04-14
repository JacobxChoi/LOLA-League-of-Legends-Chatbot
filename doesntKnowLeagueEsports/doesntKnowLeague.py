
from .IntroduceLeague import IntroduceLeague
from .laneInfo import laneInfo

IntroduceLeague = IntroduceLeague()
laneInfo = laneInfo()


def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeagueEsports',
        '`Have you ever played League of Legends?`': {
            'state': 'playedLOL',
            '[{yes, yeah, yup}]': {
                'state': 'familiarity',
                '`Who\'s your favorite champion?`': {
                    '#UserChamp': {
                        # ontology for favorite champion. Does not unfortunately handle cases where user has no favorite champion
                        '$FAV_CHAMP `is fun to play!` $PLAYER_RECOMMEND`plays them as well.`': 'end'
                    },
                    '[{dont, no}]': {
                        '`All good. My favorite champion is Irelia. I like playing aggressively and getting kills, so I find playing Irelia pretty fun.`': 'end'
                    },
                    'error': 'end'
                }
            },
            # TODO: add new branch here
            '[{heard, [video game]}]': {
                '`Yeah, it\'s actually one of the most popular video games in the world! It\'s a competitive, team-based game that\'s played by millions of people, and it has a thriving e-sports scene.`':  {
                    '[esport]': {

                    }
                }
            },
            '[{no, nope, not, dont, never, barely, little bit}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                #TODO: rewrite the casual converstaion part to add depth and smooth transitions
                '#GATE `What\'s your favorite game?`': {
                    # TODO: catch circumstance if the user do not have favorite game
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME `. `': 'transit'
                    },
                    'error':{
                        '`Cool`': 'transit'
                    }
                },

                '#GATE `Why are you interested in League esports?`': {
                    'state': 'interest',
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
                                # TODO to add different attitude toward different games
                                '`(^ρ^)/, Wow,I love` #GET_SportsEvent `too. My emotion get quickly driven by the players, and I love that feeling !`': {
                                    '[{too, [as well]}, yeah, sure, true]': {
                                        'score': '0.5',
                                        '`Hmm, I don\'t know where the excitement exactly come from, but I did feel connected when I watched the sport event, even it\'s online. `': {

                                            '[{yeah,well,true,too}]': {
                                                '`What do you think of esport event then`': {
                                                    '[{wont, not, hard }]': {

                                                    },


                                                }

                                            },
                                            'error': {
                                                '`Cool, in this case what do you think about the esport event of virtual games?`': 'esportAttitude',
                                            }

                                        }
                                    }
                                },

                                'error': {
                                    '`Cool, in this case what do you think about the esports event of virtual games?`': {
                                        'state': 'esportAttitude',
                                    }
                                }

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
                    '[{not, not really, no, dont, nothing}]': {
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

                '`Have you heard of the game league of legend before ?`':{

                }



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

    return doesntKnowLeague, items, base, laneInfo, IntroduceLeague
