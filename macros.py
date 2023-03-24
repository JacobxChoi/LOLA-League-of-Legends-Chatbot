import json
import spacy

from emora_stdm import Macro, Ngrams
from typing import Dict, Any, List
import re
import random

class MacroEsportsOrLeague(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        r = re.compile(r"(dont.*play(?:ing)*)|([lL]eague(?:\s)*(?:[oO]f [lL]egend(?:s)?)?)?")
        # m = r.search(ngrams.text())
        hasLeague = False
        for m in re.finditer(r, ngrams.text()):
            if m.group(1) or m.group(2) is not None:
                hasLeague = True
        return hasLeague

# class lolasFavChamp(Macro):
#     def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
#         # json.load('resources/teams.json')
#         f = open('resources/teams.json')
#         data = json.load(f)
#
#         for player in ngrams:
#             for _, teams in data['ontology'].items():
#                 for pro in teams:
#                     if player == pro:
#                         vars['FAV_PLAYER'] = pro
#                         return True
#         return False

class UserInfo(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        #variables used in conversation so far.
        #TODO We don't need to intialize the variables here, but it might be good to keep track of which variables we use
        visits = 'VISITS'
        player = 'FAV_PLAYER'
        playerRec = 'PLAYER_RECOMMEND'
        champ = 'FAV_CHAMP'
        vars[champ] = ''
        vars[player] = ''
        vars[playerRec] = ''
        vars[visits] = 1

class UserInputChampion(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):

        #variables
        playerRec = 'PLAYER_RECOMMEND'
        fav_champ = 'FAV_CHAMP'

        #opening jason
        f = open('resources/champs.json', )
        data = json.load(f)
        #takes user input as string
        mystr = ngrams.text()

        #loads spacy model to tokenize string
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(mystr)

        #turns user input into a list of strings
        sentenceSplit = mystr.split()

        #top, mid, jungle, bot, support
        for role in data['ontology']['lane']:
            #iterates through each champion
            for champion in data['ontology'][role]:
                #for each token in user's sentence
                for token in doc:
                    #champions are labeled as nouns by spacy
                    if token.pos_ == 'NOUN':
                        #if champion in ontology and player suggested champion is same as champion in iteration
                        if token.text in data['ontology'] and champion == token.text:
                            #keeps track of first player in ont who plays that champion in lcs
                            #TODO keep track of recommended players
                            #TODO handle cases where user does not have favorite champ
                            #TODO handle cases where user misspells champion
                            vars[fav_champ] = champion
                            vars[playerRec] = data['ontology'][token.text][0]
                            break
                else:
                    continue  # only executed if the inner loop did NOT break
                break
            else:
                continue  # only executed if the inner loop did NOT break
            break
        return True


class MacroRandNum(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        randomNum = random.randint(0,1)
        if randomNum==1:
            print('yes')
            return True
        else:
            return False