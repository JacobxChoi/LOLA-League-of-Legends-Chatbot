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
                    '#UserChamp': {  # ontology for favorite champion. Does not unfortunately handle cases where user has no favorite champion
                        '$FAV_CHAMP `is fun to play!` $PLAYER_RECOMMEND`plays them as well, and they\'re really fun to watch. I suggest watching them`': 'end'
                    },
                    '[{no, not really, not}]': {
                        '`All good. My favorite champion is Irelia. I like playing aggressively and getting kills, so I find playing Irelia pretty fun.`': 'end'
                    },
                    'error': 'end'
                }
            },
            '[{no, not, dont}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                '#GATE `What\'s your favorite game type`': {
                    '[$FAV_GAME=#ONT(gametype)]': {
                        '`I love` $FAV_GAME `too !`': 'transit'
                    },
                    'error':{
                        '`I love them too!`': 'transit',
                    }
                },

                '#GATE `Why are you interested at league e-Sports`': {
                    'state': 'interest',
                    '[{friend,social,community}]': {
                        '`Yeah, It\'s great to find some hallucinating identity in the online community `': 'transit'
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
                        '`I like` $FAV_PLAYER `too`': 'transit'
                    },
                    '[{not,not really, no}]': {
                        '`Well, so I guess you just want to get some infos in the area`': 'transit'
                    },
                    'error': {
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                    '[{bye,exit}]': {
                        'state': 'quit',
                        '`Adieu,hope to see you again`': 'end'
                    },
                },
                '`Do you want to know more about the game?`': 'end',
            },
            'error': {
                'Sorry, human languages are sometimes mysterious for me. Could you repeat your request ?': 'transit'
            },

        },

    }

    items = {
        'state': 'items',
        '`Items are intimidating at first glance, but they\'re actually pretty simple.`': 'end'  # TODO: add info about items
    }

    base = {
        'state': 'base',
        '`Each team has their base at opposite corners of the map. The base is where players respawn after getting '
        'killed, as well as where they can heal their HP and buy items. The nexus is in the center of the base, '
        'protected by 2 turrets which do massive damage to champions in their range. Once one team destroys their '
        'opponents nexus, they win the game.`': 'end'
    }

    return doesntKnowLeague, items, base, laneInfo
