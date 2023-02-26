from emora_stdm import DialogueFlow
from src.project.knowsLeague import knowsLeague
from src.project.doesntKnowLeague import doesntKnowLeague
from src.project.macros import MacroEsportsOrLeague

favoriteTeam, favoriteRegion = knowsLeague()
doesntKnowLeague = doesntKnowLeague()

transitions = {
    'state':'start',
    '`Do you know much about League of Legends esports?`':{
        '[yes]': {
            '`nice.`': 'favRegion', #error. I thought it would pick randomly, but only picks the bottom option, so 'favTeam' in this example
            '`nice.`': 'favTeam'
        },
        '#IF(#LEAGUE)':'explainLeague',
        '[{no, not, dont}]':'doesntKnowLeague', #change 'no' to something like: no, I don't really play league.
        'error':{
            '`Sorry, I didn\'t understand you.`':'start'
        }
    }
}

macros = {
    'LEAGUE' :  MacroEsportsOrLeague()
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('teams.json')
df.load_transitions(transitions)
df.load_transitions(favoriteTeam)
df.load_transitions(favoriteRegion)
df.load_transitions(doesntKnowLeague)
df.add_macros(macros)

if __name__ == '__main__':
    df.run()