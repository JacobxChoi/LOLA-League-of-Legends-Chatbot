from doesntKnowLeague.buildInfo import buildInfo
from doesntKnowLeague.champInfo import championInfo
from doesntKnowLeague.laneInfo import laneInfo


def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeague',
        '`That\'s fine. Do you play League of Legends?.`': {
            '[{yes, yeah}]': {
                'state': 'familiarity',
                '`Who\'s your favorite champion?`': {
                    '[favorite champion]': {  # ontology for favorite champion
                        '`That champion is fun to play! This esports player plays them as well, and they\'re really fun to watch. I suggest watching them`': 'end'
                    },
                    'error': 'end'
                }
            },
            '[{no, not, dont}]': {
                'state': 'explainLeague',
                '`That\'s fine. League is just an online 5 v 5 game, where players play champions that each have unique abilites, and the objective of the game is to kill the enemy player\'s nexus. Do you have some specific questions?`': {
                    '[yes]': {
                        '`Nice! What got you interested in League?`': {
                            '[any response]': {
                                '`That\'s awesome! If you want to learn more, you should watch this player. He\'s pretty famous in the community, and I think it would be a good way to learn about the community.`': 'end'
                            },
                            'error': 'end'
                        }
                    },
                    '[no]': {
                        '`What are you confused about?`': {
                            '[lane]': 'laneRole'
                        }
                    },
                    'error': 'end'
                }
            },
            'error': 'doesntKnowLeague'
        }
    }

    laneRole = {
        'state': 'laneRole',
        '`Yeah, there are 5 lanes in a typical League game, and players for each lane have very different Roles`': {
            '[{5, five}, lanes]': {
                '`You maybe heard some of them, and they are Top, Jungle, Mid, ADC and Support. People often choose '
                'their favorite lanes according to their personality and unique playing habits. They often jump '
                ' between the roles for better team cooperation. `'
                : {
                    '[TOP]': {
                        'state': 'topLane',
                        '`TOP lane is often considered as the Lone Wolf. If you are a 1v1 enthusiasts who want to '
                        'lean on your own skills and tactics to win the game by pouring tons of pressures on   '
                        'your foes. It\'s a great choice for you!`': {

                            '[{enjoy, yes}]': {
                                'state': 'topArchetypes',
                                '`Great! Sounds like you are an 1v1 combat fans who want to overwhelm you foes with '
                                'superb skills. There are actually several archetypes for a typical top lane '
                                'champion, like tanks and duelists. Do you want to know more about them? `': {
                                    '[tank]': 'end',  # TODO add infos on tank
                                    '[duelist]': 'end',  # TODO add infos on duelists
                                    'error' : 'end'
                                }

                            },
                            'error': 'end'

                        }
                    },
                    'error' : 'end'
                }
            },
            'error' : 'end'# TODO: modify the diagram flow for more flexible transitions

        }

    }
    return doesntKnowLeague, laneRole
