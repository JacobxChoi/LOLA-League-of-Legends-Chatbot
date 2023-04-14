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
                '`Yeah, it\'s actually one of the most popular video games in the world! It\'s a competitive, team-based game that\'s played by millions of people, and it has a thriving e-sports scene. Would you like to learn more about the game or the esports scene?`': {
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }
            },
            '[{no, nope, not, dont, never, barely, little bit}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                # TODO: rewrite the casual converstaion part to add depth and smooth transitions
                '#GATE `What\'s your favorite game?`': {
                    # TODO: catch circumstance if the user do not have favorite game
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME `. `': 'transit'
                    },
                    'error': {
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

                '`Let me give you a brief introduction to League of Legends. It\'s a multiplayer online battle arena (MOBA) game where two teams of five players compete against each other with the goal of destroying the enemy team\'s base, called the Nexus. Each player controls a unique character, called a champion, with special abilities and roles. Champions become more powerful as the game progresses by earning experience and gold. Do you want to know more about the game mechanics or the esports scene?`': {
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }

            },

            'error': {
                '`Sorry, I didn\'t catch that, could you say it again? ξ( ✿＞◡❛)`': 'playedLOL'
            },

        },

    }
    
    IntroduceGame = {
        'state': 'IntroduceGame',
        '`There are three main roles in the game: damage dealers (called AD Carry or APC), tanks, and supports. Damage dealers focus on dealing damage to enemy champions, tanks absorb damage and protect their teammates, and supports provide utility to their team through healing, crowd control, and vision control. The map is divided into three lanes and a jungle area. Players must work together, communicate, and strategize to secure objectives and outplay their opponents. Would you like to know about the different types of champions or the in-game objectives?`': {
            '[{champions, types}]': 'IntroduceChampions',
            '[{objectives, in-game}]': 'IntroduceObjectives',
            'error': 'IntroduceChampions'
        }
    }

    IntroduceChampions = {
        'state': 'IntroduceChampions',
        '`There are over 150 champions in League of Legends, and they can be categorized into six main classes: assassins, fighters, mages, marksmen, supports, and tanks. Each class has its own unique playstyle and abilities. Assassins are mobile and deal high burst damage, fighters excel in close combat, mages use powerful spells, marksmen deal sustained ranged damage, supports provide utility and protection, and tanks are durable front-liners. Are you interested in learning about specific champions or the roles they play in a team?`': {
            '[{specific, champions}]': 'SpecificChampions',
            '[{roles, team}]': 'ChampionRoles',
            'error': 'SpecificChampions'
        }
    }

    SpecificChampions = {
        'state': 'SpecificChampions',
        '`Some popular champions for beginners include Garen (a tanky fighter), Ashe (a marksman), and Lux (a mage). These champions have relatively simple mechanics, making it easier for new players to learn the game. If you\'re interested, I can recommend more champions for each role.Would you like that?`': {
            '[{yes, sure, recommend}]': 'RecommendChampions',
            '[{no, not now, later}]': 'EndSpecificChampions',
            'error': 'RecommendChampions'
        }
    }

    RecommendChampions = {
        'state': 'RecommendChampions',
        '`Here are some champion recommendations for each role: Top: Garen, Malphite, and Darius - Jungle: Warwick, Amumu, and Vi - Mid: Annie, Lux, and Veigar - ADC: Ashe, Miss Fortune, and Sivir - Support: Soraka, Leona, and Morgana These champions have straightforward abilities and are great for beginners.Don\'t forget to try out different champions to find the ones that best suit your playstyle. Are you interested in learning about the in-game objectives?`': {
            '[{yes, objectives, sure}]': 'IntroduceObjectives',
            '[{no, not now, later}]': 'EndObjectives',
            'error': 'IntroduceObjectives'
        }
    }

    ChampionRoles = {
        'state': 'ChampionRoles',
        '`In a team, champions play specific roles based on their strengths and abilities. The roles are: Top, Jungle, Mid, ADC, and Support. Top laners are usually tanks or fighters, junglers roam the map and secure objectives, mid laners are mages or assassins, ADCs deal consistent damage from range, and supports protect their team and provide utility. Each role contributes to the overall success of the team. Are you interested in learning about the in-game objectives?`': {
            '[{yes, objectives, sure}]': 'IntroduceObjectives',
            '[{no, not now, later}]': 'EndObjectives',
            'error': 'IntroduceObjectives'
        }
    }

    IntroduceObjectives = {
        'state': 'IntroduceObjectives',
        '`In-game objectives are crucial to winning in League of Legends. The main objectives are turrets, inhibitors, dragons, the Rift Herald, Baron Nashor, and the enemy Nexus. Turrets and inhibitors defend each team\'s base, while dragons and the Rift Herald grant powerful buffs to the team that defeats them.Baron Nashor grants a powerful buff to the entire team, helping them push lanes and destroy the enemy base.Ultimately, the goal is to destroy the enemy Nexus.Would you like to know more about the esports scene or are you ready to try the game?`': {
            '[{esports, scene}]': 'IntroduceEsports',
            '[{try, game}]': 'ReadyToTry',
            'error': 'IntroduceEsports'

        }
    }

    IntroduceEsports = {
        'state': 'IntroduceEsports',
        '`League of Legends esports is a highly competitive scene with regional and international tournaments. The most prestigious event is the League of Legends World Championship, where the best teams from around the world compete for the title of world champion. Regional leagues, like the LCS (North America), LEC (Europe), LPL (China), and LCK (Korea), have regular seasons and playoffs that lead to international events. Top players can earn fame, fortune, and the adoration of fans. Would you like to learn more about specific teams or players?`': {
            '[{teams, specific}]': 'SpecificTeams',
            '[{players, specific}]': 'SpecificPlayers',
            '[{no, not now, later}]': 'EndEsports',
            'error': 'SpecificTeams'
        }
    }

    SpecificTeams = {
        'state': 'SpecificTeams',
        '`Some of the most famous and successful teams in League of Legends history include T1 (formerly SK Telecom T1) from Korea, Fnatic and G2 Esports from Europe, and Team SoloMid and Cloud9 from North America. These teams have consistently performed well in their regional leagues and at international events. Are you interested in learning about specific players?`': {
            '[{yes, players, specific}]': 'SpecificPlayers',
            '[{no, not now, later}]': 'EndPlayers',
            'error': 'SpecificPlayers'
        }
    }

    SpecificPlayers = {
        'state': 'SpecificPlayers',
        '`Some legendary players in the history of League of Legends esports are Faker (mid laner for T1), Uzi (former ADC for Royal Never Give Up), Caps (mid laner for G2 Esports), and Doublelift (former ADC for Team SoloMid and Team Liquid). These players have had successful careers and have made a significant impact on the esports scene. I hope this information has been helpful. Are you ready to try the game now?`': {
            '[{yes, try, game}]': 'ReadyToTry',
            '[{no, not now, later}]': 'EndReadyToTry',
            'error': 'ReadyToTry'
        }
    }

    ReadyToTry = {
        'state': 'ReadyToTry',
        '`Great! You can download League of Legends for free from the official website. It\'s available on Windows and macOS.I hope you have fun exploring the game and finding your favorite champions.If you have any more questions, don\'t hesitate to ask!`': 'end'
    }

    EndSpecificChampions = {
        'state': 'EndSpecificChampions',
        '`Alright, if you have any more questions about champions or anything else related to League of Legends, feel free to ask anytime. Have fun exploring the game!`': 'end'
    }

    EndObjectives = {
        'state': 'EndObjectives',
        '`No problem! If you have more questions about in-game objectives or anything else related to League of Legends, don\'t hesitate to ask.Enjoy your time in the game!`': 'end'
    }

    EndEsports = {
        'state': 'EndEsports',
        '`That\'s totally fine! If you ever want to learn more about the esports scene or anything else related to League of Legends, feel free to ask.Have a great time playing the game!`': 'end'
    }

    EndPlayers = {
        'state': 'EndPlayers',
        '`Okay! If you ever want to know more about specific players or anything else related to League of Legends, just let me know. Enjoy your journey into the world of League of Legends!`': 'end'
    }

    EndReadyToTry = {
        'state': 'EndReadyToTry',
        '`No worries! If you ever decide to give League of Legends a try, or if you have any more questions, feel free to ask. Have a great day!`': 'end'
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

    return doesntKnowLeague, items, base, laneInfo, IntroduceLeague, IntroduceGame, IntroduceChampions, IntroduceEsports, IntroduceObjectives, ChampionRoles, SpecificTeams, SpecificChampions, SpecificPlayers, RecommendChampions, ReadyToTry, EndReadyToTry, EndPlayers, EndEsports, EndObjectives, EndSpecificChampions
