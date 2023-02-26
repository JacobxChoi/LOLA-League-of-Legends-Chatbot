from emora_stdm import DialogueFlow
from src.project.knowsLeague import knowsLeague
from src.project.doesntKnowLeague import doesntKnowLeague

favoriteTeam, favoriteRegion = knowsLeague()
doesntKnowLeague = doesntKnowLeague()

transitions = {
    'state':'start',
    '`Do you know much about League of Legends esports??`':{
        '[yes]': {
            '`nice.`': 'favRegion', #error. I thought it would pick randomly, but only picks the bottom option, so 'favTeam' in this example
            '`nice.`': 'favTeam'
        },
        '[no]':'doesntKnowLeague', #change 'no' to something like: no, I don't really play league.
        'error':{
            '`Sorry, I didn\'t understand you.`':'start'
        }
    }
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('teams.json')
df.load_transitions(transitions)
df.load_transitions(favoriteTeam)
df.load_transitions(favoriteRegion)
df.load_transitions(doesntKnowLeague)

if __name__ == '__main__':
    df.run()