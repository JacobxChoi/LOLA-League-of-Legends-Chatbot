
def globalState():
    global_transitions = {
        '[{covid, corona, virus}]': {
            '`I hope you are OK.`': 'good'
        },
        '[{birthday}]': {
            '`Happy birthday to you!`': 'good'
        },
        '[introduce league]':{
            'score':2,
            '`Test start`': 'IntroduceLeague'
        },
        '[directed question]':{
            'score': 2,
            '`Test start`': 'Directed_Questions'
        },
    }
    return global_transitions