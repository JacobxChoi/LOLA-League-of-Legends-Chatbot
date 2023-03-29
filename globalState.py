
def globalState():
    global_transitions = {
        '[{covid, corona, virus}]': {
            '`I hope you are OK.`': 'good'
        },
        '[{birthday}]': {
            '`Happy birthday to you!`': 'good'
        }
    }
    return global_transitions