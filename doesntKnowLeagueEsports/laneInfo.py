def laneInfo():
    laneInfo = {
        'state': 'laneInfo',
        '`So there are 3 lanes in League, and the 5 players on each team each fill 1 role and are distributed across those 3 lanes.`': {
            '[{3, three}, lanes]': {
                '`You may have heard about them, the lanes are Top, Middle, or Mid, and Bottom, or Bot. The last 2 '
                'players fill the Support and Jungle roles. People often choose their favorite lanes based to their personality '
                'and unique playing habits. In higher ranks, players will swap between roles from game to game, and across '
                'lanes within a single game. Which lane would you like to hear more about?`': {
                    '[top]': {
                        'state': 'topLane',
                        '`Top lane is often considered as the Lone Wolf. If you are a 1v1 enthusiast who wants to '
                        'lean on your own skills and tactics to win the game by pouring tons of pressure on   '
                        'your foes, then it\'s a great choice for you!`': {
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
                    '[mid, middle]': {
                        '`Mid lane is usually filled by fast, high damage champions. If you like playing quickly and '
                        'dealing a lot of burst damage, then Mid would be a great choice for you!`': {
                            '[{enjoy, yes}]': {
                                'state': 'midArchetypes',
                                '`Nice, seems you like the sound of Mid lane! Most Mid lane champions are mages that '
                                'focus on ability power, but there are some that focus more on physical attacks. '
                                'Do you want to know more about these champs?`': {
                                    '[{mage, ability power}]': 'end',  # TODO: add infos on AP carries
                                    '[physical]': 'end',  # TODO: add infos on AD mid lane champs
                                    'error': 'end'
                                }

                            },
                            'error': 'end'
                        }
                    },
                    '[bot, bottom, adc, support, supp]': {
                        '`Bot lane is the only lane with 2 champions from each team in it. The main damage dealer in Bot '
                        'is also sometimes called the Attack Damage Carry, or ADC, since they\'re usually focused on '
                        'doing a lot of damage. The second champion fills the Support role. They\'re focused on helping '
                        'their team maintain vision of the map, as well as supporting the ADC in Bot lane and their '
                        'team in team fights. Would you like to hear more about either of these roles?`': {
                            '[{adc}]': {
                                'state': 'adcArchetypes'
                            },
                            '[{supp, support}]': {
                                'state': 'suppArchetypes'
                            },
                            'error': 'end'
                        }
                    },
                    '[jungle, jg]': {
                        '`The Jungler is focused on defeating neutral monsters in the jungle to collect buffs for their '
                        'team. They also roam between lanes to support their teammates in their individual lanes, which '
                        'is also called ganking. If you like being active across the whole map, then Jungle would be a '
                        'great choice for you!`': {
                            '[{enjoy, yes}]': {
                                'state': 'jgArchetypes',
                                '`Cool! Looks like you would be into Jungle! While all Junglers farm and gank, each is '
                                'focused more on one of the two aspects. Would you like to hear about the 2 types of '
                                'Junglers?`': {
                                    '[{roam, gank, ganking, ganks}]': 'end',  # TODO: add infos on gankers
                                    '[{farm, creeps, monsters}]': 'end',  # TODO: add infos on farmers
                                    'error': 'end'
                                }

                            },
                        }
                    },
                    'error': 'end'
                }
            },
            'error': 'end'  # TODO: modify the diagram flow for more flexible transitions

        }

    }
    return laneInfo