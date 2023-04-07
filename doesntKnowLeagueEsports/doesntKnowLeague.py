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
                        '$FAV_CHAMP `is fun to play!` $PLAYER_RECOMMEND`plays them as well, and they\'re really fun to watch. I suggest watching them`': 'end'
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
                '#GATE `What\'s your favorite game `': {
                    'score': '1',
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME': 'transit'
                    },
                    'error': {
                        '`Sounds like an interesting game, I\'ll definitely try it some day!`': 'transit',
                    }
                },

                '#GATE `Why are you interested at league e-Sports`': {
                    'state': 'interest',
                    'score': '0.8',
                    '[{friend, friends, social, community}]': {
                        '`Yeah, a shared interest in game connects friends together. What are you typically do with friends in free time?`': {
                            '[#ACTIVITY_WITH_FRIENDS]': {
                                '`Definitely, I wish I would have chance to` #GET_ACTIVITY_FRIEND ` with my friends too`': 'transit'
                            },
                        }
                    },
                    '[{fun,challenging,exciting}]': {
                        '`For sure! After all, the adrenaline rush after watching an exciting matches is true `': 'transit'
                    },

                    '[{waste, time}]': {
                        '`Ha, Sounds like you have fallen into the trap of modernism. I guess there would be better '
                        'ways to use time`': 'transit'
                    },

                    '[$FAV_PLAYER=#ONT(leagues)]': {
                        '#IF($FAV_PLAYER = jojopyun) `Agree! Jojopyan is my favorite player too`': 'transit',
                        '`I like` $FAV_PLAYER `too`': 'transit',
                        'error': 'loveLeague',
                    },
                    '[{not,not really, no}]': {
                        '`Well, so I guess you just want to get some infos in the area.`': 'transit'
                    },
                    '[{bye,exit}]': {
                        'state': 'quit',
                        '`Adieu,hope to see you again`': 'end'
                    },
                    'error': {
                        'state': 'loveLeague',
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                },

                '`Do you want to know more about the league of legends. I can give you a brief introduction over the '
                'game goal, champion selection and some advice for improving in-game skills`': {
                    'state': 'IntroduceLeague',
                    'score': '0.5',

                    '[{goal, win}]': 'GameGoal',
                    '[{#LEM(improve), enhance}]': 'howToImprove',
                    '[{champion}]': 'champInfo',
                    '[{role,lane}]': 'roleInfo',
                    '[{map}]': 'mapInfo',
                    'error': {
                        '`Sorry, I don\'t understand you, could you say it again?`': 'IntroduceLeague'
                    }
                },

            },

            'error': {
                '`Sorry, I don\'t understand you, could you say it again?`': 'transit'
            },

        },

    }

    items = {
        'state': 'items',
        '`Items are intimidating at first glance, but they\'re actually pretty simple.`': 'end'
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