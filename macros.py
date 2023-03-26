import json
import spacy

from emora_stdm import Macro, Ngrams
from typing import Dict, Any, List
import re
import random

class MacroGetName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):

        ##TODO accept more expresisons
        r = re.compile(r"(?:call me)?(mr|ms|mrs|dr)?(?:^|\s)([a-z']+)(?:\s([a-z']+))?")
        m = r.search(ngrams.text())
        if m is None: return False

        title, firstname, lastname = None, None, None

        if m.group(1):
            title = m.group(1)
            if m.group(3):
                firstname = m.group(2)
                lastname = m.group(3)
            else:
                firstname = m.group()
                lastname = m.group(2)
        else:
            firstname = m.group(2)
            lastname = m.group(3)

        vars['TITLE'] = title
        vars['LASTNAME'] = lastname
        vn_FN = 'FIRSTNAME'

        vn_firstname = firstname.capitalize()

        if vn_FN not in vars:
            vars[vn_FN] = firstname
            vars[vn_firstname] = False

        if vn_firstname not in vars['FIRSTNAME']:
            vars['FIRSTNAME'] = vn_firstname
            vars[vn_firstname] = False

        else:
            vars[vn_firstname] = True
        return True


class MacroGetOldName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        vn = vars['FIRSTNAME']
        return vars[vn]


class MacroGetNewName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        vn = vars['FIRSTNAME']
        return not vars[vn]

class MacroPushName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        return vars['FIRSTNAME']

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

class favRegion(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        #opens json
        f = open('resources/tourneys.json', )
        data = json.load(f)

        #gets user input
        mystr = ngrams.text()

        #spacy to find nouns in user input
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(mystr)

        #different ways a user can reference the regions
        regions = {'na': 'NORTH AMERICA',
                   'north america': 'NORTH AMERICA',
                   'north': 'NORTH AMERICA',
                   'america': 'NORTH AMERICA',
                   'north american': 'NORTH AMERICA',
                   'kr': 'KOREA',
                   'korea': 'KOREA',
                   'emea': 'EMEA',
                   'latam': 'LATIN AMERICA',
                   'hong kong': 'HONG KONG, MACAU, TAIWAN',
                   'macau': 'HONG KONG, MACAU, TAIWAN',
                   'taiwan': 'HONG KONG, MACAU, TAIWAN',
                   'cis': 'COMMONWEALTH OF INDEPENDENT STATES',
                   'tr': 'TURKEY',
                   'turkey': 'TURKEY',
                   'vt': 'VIETNAM',
                   'vietnam': 'VIETNAM',
                   'oc': 'OCEANIA',
                   'oceania': 'OCEANIA',
                   'international': 'INTERNATIONAL',
                   'br': 'BRAZIL',
                   'brazil': 'BRAZIL',
                   'cn': 'CHINA',
                   'china': 'CHINA',
                   'jp': 'JAPAN',
                   'japan': 'JAPAN'
        }

        # labeled T because they're temporary variables that are not meant to be stored.
        # TODO make a macro to remove unnecessary variables

        region = 'T_REGION'
        tourney = 'T_TOURNEY'
        typeOfMatch = 'T_MATCH'
        team1 = 'T_TEAM1'
        team2 = 'T_TEAM2'
        winner = 'T_WINNER'
        date = 'T_DATE'
        month = 'T_MONTH'
        day = 'T_DAY'

        vars[region] = ''
        vars[tourney] = ''
        vars[typeOfMatch] = ''
        vars[team1] = ''
        vars[team2] = ''
        vars[winner] = ''
        vars[date] = ''
        vars[month] = ''
        vars[day] = ''

        #region local variable
        region = ''

        #finds nouns
        listNouns = []
        for token in doc:
            print(token.text, token.pos_)
            if token.pos_ == 'PROPN' or token.pos_ == 'NOUN':
                print(token.pos_)
                listNouns.append(token.text)

        #sees if nouns match region dictionary and retrieves region
        for noun in listNouns:
            if noun.lower() in regions:
                region = regions[noun.lower()]


        #no region found. Return false
        if region == '':
            print('returned false 1')
            return False

        #some regions don't have any games from this year so far. If this is the case, return false
        if (len(data['ontology'][region]) >= 1):
            tourney = data['ontology'][region][0]
        else:
            print('returned false 2')
            return False

        #pulling game info from ontology. Last index -1 means most recent game. LOLA should remember which game was suggested
        #TODO remember which games were suggested
        game = data['ontology'][tourney][-1]

        vars[typeOfMatch] = game['week']
        vars[team1] = game['teams'][0]
        vars[team2] = game['teams'][1]
        vars[winner] = game['winner']
        vars[date] = game['time'][0:10]
        vars[month] = date[5:7]
        vars[day] = date[-2:]

        #playoffs
        if typeOfMatch[0:8] == 'Playoffs':
            vars[typeOfMatch] = typeOfMatch[-7:].lower() + " " + typeOfMatch[0:8].lower()
        #knockout or weekly games
        else:
            vars[typeOfMatch] = typeOfMatch.lower()

        #change numerical month to month name
        if month == '01':
            vars[month] = 'January'
        elif month == '02':
            vars[month] = 'February'
        elif month == '03':
            vars[month] = 'March'
        elif month == '04':
            vars[month] = 'April'

        # rd, st, th for days
        if day[-1:] == '2' or day[-1:] == '3':
            vars[day] = day + "rd"
        elif day[-1:] == 1:
            vars[day] = day + "st"
        else:
            vars[day] = day + "th"

        return True
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
        nlp = spacy.load("en_core_web_md")
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
                            #TODO handle cases where user has multiple favorite champions
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