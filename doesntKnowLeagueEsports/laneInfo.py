def laneInfo():
    laneInfo = {
        'state': 'laneInfo',
        '`So there are 3 lanes in League, and the 5 players for each team each fill 1 role and are distributed across those 3 lanes`': {
            '[{3, three}, lanes]': {
                '`You maybe heard some of them, and they are Top, Mid, and Bottom. Added support and Jungle. There '
                'are 5 roles in total. People often choose their favorite lanes according to their personality and '
                'unique playing habits. They often jump between the roles for better team cooperation. `'
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
                                    '[tank]': 'end',  # TODO: add infos on tank
                                    '[duelist]': 'end',  # TODO: add infos on duelists
                                    'error': 'end'
                                }

                            },
                            'error': 'end'

                        }
                    },
                    'error': 'end'
                }
            },
            'error': 'end'  # TODO: modify the diagram flow for more flexible transitions

        }

    }
    return laneInfo