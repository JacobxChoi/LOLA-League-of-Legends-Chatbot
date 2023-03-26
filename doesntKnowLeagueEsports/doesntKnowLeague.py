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
                'state': 'explainLeague',
                '`No problem. League is an online 5 vs 5 game, where players play "champions" that each have unique '
                'abilites. The objective of the game is to get to the opposing team\'s base and destroy their nexus. '
                'Do you have questions about any of that?`': {
                    '[{no, nope, not really}]': {
                        '`Nice! What got you interested in League?`': {
                            'error': {
                                '`That\'s awesome! If you want to learn more, you should watch this player. He\'s pretty famous in the community, and I think it would be a good way to learn about the community.`': 'end'
                            }
                        }
                    },
                    '[{yes, yeah, kind of, kinda}]': {
                        '`What are you confused about?`': {
                            '[{lane, role}]': 'laneInfo',
                            '[{item}]': 'items',
                            '[{champion, champ}]': 'championInfo',
                            '[{base, nexus}]': 'base'
                        }
                    },
                    'error': 'doesntKnowLeagueEsports'
                }
            },

        }
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
