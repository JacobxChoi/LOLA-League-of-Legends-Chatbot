from emora_stdm import DialogueFlow
from src.project.knowsLeague import knowsLeague
from src.project.doesntKnowLeague import doesntKnowLeague

knowsLeague = knowsLeague()
doesntKnowLeague = doesntKnowLeague()

transitions = {
    'state':'start',
    '`Do you know anything  about League of Legends?`':{
        '[yes]':'knowsLeague', #change 'yes' to something like: yeah, I like playing league.
        '[no]':'doesntKnowLeague', #change 'no' to something like: no, I don't really play league.
        'error':{
            '`Sorry, I didn\'t understand you.`':'start'
        }
    }
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('teams.json')
df.load_transitions(transitions)
df.load_transitions(knowsLeague)
df.load_transitions(doesntKnowLeague)

if __name__ == '__main__':
    df.run()