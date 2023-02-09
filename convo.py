from emora_stdm import DialogueFlow

transitions = {
    'state': 'start',
    '`What is your favorite team?`': {
        '[{$FAVORITE_TEAM=#ONT(lpl)}]':{
            '`Glad to hear that you are doing well :)`': {
                'error': {
                    '`See you later!`': 'end'
                }
            }
        },
        'error': {
            '`I hope your day gets better soon :(`': {
                'error': {
                    '`Take care!`': 'end'
                }
            }
        }
    }
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('games.json')
df.load_transitions(transitions)

if __name__ == '__main__':
    df.run()