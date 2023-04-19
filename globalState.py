
def globalState():
    global_transitions = {
        '[{covid, corona, virus}]': {
            'score':2,
            '`I hope you are OK.`': 'good'
        },
        '[{birthday}]': {
            'score': 2,
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
        '[haiku]':{
            'score': 2,
            '#GET_HAIKU $HAIKU':'DIVERGE'
        },
        '[babel]':{
            'score':2,
            '`Sure!`':'babel'
        }
    }
    return global_transitions