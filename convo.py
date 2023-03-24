from emora_stdm import DialogueFlow
from knowsLeague import knowsLeague
from doesntKnowLeague.doesntKnowLeague import doesntKnowLeague
from macros import MacroEsportsOrLeague, MacroRandNum
from doesntKnowLeague.buildInfo import buildInfo
from doesntKnowLeague.champInfo import championInfo
from doesntKnowLeague.laneInfo import laneInfo
import pickle
import os

# buildInfo = buildInfo()
favoriteTeam, favoriteRegion = knowsLeague()
doesntKnowLeague, laneRole = doesntKnowLeague()

def save(df: DialogueFlow, varfile: str):
    df.run()
    d = {k: v for k, v in df.vars().items() if not k.startswith('_')}
    pickle.dump(d, open(varfile, 'wb'))

def load(df: DialogueFlow, varfile: str):
    #has conversed before
    if os.path.isfile('resources/visits.pkl'):
        d = pickle.load(open(varfile, 'rb'))
        df.vars().update(d)
        df.run()
        save(df, varfile)
    # first time
    else:
        df.run()
        save(df, varfile)


transitions = {
    'state':'start',
    '`Do you know much about League of Legends esports?`':{
        '[{yes, yeah, know}]': {
            '`nice.`': 'favPlayer',
        },
        '[{no, not, dont}]':'doesntKnowLeague', #change 'no' to something like: no, I don't really play league.
        'error':{
            '`Sorry, I didn\'t understand you.`':'start'
        }
    }
}

macros = {
    'LEAGUE' :  MacroEsportsOrLeague(),
    'NUM' : MacroRandNum(),
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('resources/teams.json')
df.load_transitions(transitions)
df.load_transitions(favoriteTeam)
df.load_transitions(favoriteRegion)
df.load_transitions(doesntKnowLeague)
df.load_transitions(laneRole)
'''
df.load_transitions(championInfo)
df.load_transitions(laneInfo)
df.load_transitions(buildInfo)
'''

df.add_macros(macros)

if __name__ == '__main__':
    load(df, 'resources/visits.pkl')