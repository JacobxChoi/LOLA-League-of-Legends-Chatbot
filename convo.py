from emora_stdm import DialogueFlow
from KnowLeague.knowsLeague import knowsLeague
from doesntKnowLeagueEsports.doesntKnowLeague import doesntKnowLeague
from macros import MacroEsportsOrLeague, MacroRandNum, UserInputChampion,MacroGetName,MacroGetOldName,MacroGetNewName,MacroPushName
from doesntKnowLeagueEsports.champInfo import championInfo
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
    # has conversed before
    if os.path.isfile('resources/visits.pkl'):
        d = pickle.load(open(varfile, 'rb'))
        df.vars().update(d)
        df.run()
        save(df, varfile)
    # first time conversing
    else:
        df.run()
        save(df, varfile)


# This is the welcoming transition
transitions = {
    'state': 'start',
    ##Welcoming section TODO: Intro can be modified
    '`Hi, this is LoLa, your personal charbot for LoL esports dialogue, may I have your name`': {
        '[#GET_NAME]': {
            '#IF(#GET_NEWNAME) `Nice to meet you,` #NAME `.`': 'DIVERGE',
            '#IF(#GET_OLDNAME) `Welcome back!` #NAME `!`': 'end'  # TODO: for the same user
        }},
}

# This transition distrubutes the users to different branches of transitions based on their acquistion levels
transitionDiverging = {
    'state': 'DIVERGE',
    '`Do you know much about League of Legends esports?`': {
        '[{yes, yeah, know}]': {
            '`nice.`': 'favPlayer',
        },
        '[{no, not, dont}]': 'doesntKnowLeagueEsports',  # change 'no' to something like: no, I don't really play league.
        'error': {
            '`Sorry, I didn\'t understand you.`': 'start'
        }
    }
}

macros = {
    'LEAGUE': MacroEsportsOrLeague(),
    'NUM': MacroRandNum(),
    'UserChamp': UserInputChampion(),
    'NAME': MacroPushName(),
    'GET_NAME': MacroGetName(),
    'GET_NEWNAME': MacroGetNewName(),
    'GET_OLDNAME': MacroGetOldName(),
}

df = DialogueFlow('start', end_state='end')
df.knowledge_base().load_json_file('resources/teams.json')
df.load_transitions(transitionDiverging)
df.load_transitions(transitions)
df.load_transitions(favoriteTeam)
df.load_transitions(favoriteRegion)
df.load_transitions(doesntKnowLeague)
df.load_transitions(laneRole)

df.load_transitions(championInfo())
# df.load_transitions(laneInfo)
# df.load_transitions(buildInfo)


df.add_macros(macros)

if __name__ == '__main__':
    load(df, 'resources/visits.pkl')
