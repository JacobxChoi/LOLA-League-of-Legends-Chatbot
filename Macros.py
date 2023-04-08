import json
import random
import re
from typing import Dict, Any, List, Callable, Pattern
from json import JSONDecodeError

import spacy
from emora_stdm import Macro, Ngrams
import openai
import regexutils

OPENAI_API_KEY_PATH = 'resources/openai_api.txt'
CHATGPT_MODEL = 'gpt-3.5-turbo'


class MacroGetName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):

        r = re.compile(
            r"(?:(?:hi)?(?:\,)?(?:\s)*my(?:\s)*(?:name|nickname)(?:\s)*(?:is)?(?:\s)*|(?:hi)?(?:\,)?(?:\s)*i(?:\s)*am(?:\s)*|(?:please|you(?:\s)*can|everyone)?(?:\s)*(?:call|calls)(?:\s)*me(?:\s)*?|(?:hi)?(?:\,)?(?:\s)*i(?:\')?(?:m)?(?:ts)?(?:t\'s)?(?:\s)*(?:go by)?)?(?:\s)*(mr|mrs|ms|dr|dr\.)?(?:^|\s)*([a-z']+)(?:\s([a-z']+))?(?:(?:\,)?(?:\s)*.*)?")

        title, firstname, lastname = None, None, None

        for m in re.finditer(r, ngrams.text()):
            if m.group(1) is not None:
                title = m.group(1)
            if m.group(2) is not None:
                firstname = m.group(2)
            if m.group(3) is not None:
                lastname = m.group(3)

        if title is None and firstname is None and lastname is None:
            return False

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


class UserInfo(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        # variables used in conversation so far.
        # TODO We don't need to intialize the variables here, but it might be good to keep track of which variables we use
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
        userResponse = ngrams.text()

        # opens json
        f = open('resources/tourneys.json', )
        data = json.load(f)

        # gets user input
        mystr = ngrams.text().split()

        # different ways a user can reference the regions
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

        t_tourney = 'T_TOURNEY'
        t_typeOfMatch = 'T_MATCH'
        team1 = 'T_TEAM1'
        team2 = 'T_TEAM2'
        winner = 'T_WINNER'
        t_month = 'T_MONTH'
        t_day = 'T_DAY'

        vars[t_tourney] = ''
        vars[t_typeOfMatch] = ''
        vars[team1] = ''
        vars[team2] = ''
        vars[winner] = ''
        vars[t_day] = ''
        vars[t_month] = ''

        # region local variable
        region = ''

        # sees if nouns match region dictionary and retrieves region
        for word in mystr:
            if word.lower() in regions:
                region = regions[word.lower()]

        # no region found. Return false
        if region == '':
            return False

        # some regions don't have any games from this year so far. If this is the case, return false
        if (len(data['ontology'][region]) >= 1):
            # TODO remember regions
            tourney = data['ontology'][region][0]
            vars[t_tourney] = tourney.replace('_', ' ')
        else:
            return False

        # pulling game info from ontology. Last index -1 means most recent game. LOLA should remember which game was suggested
        # TODO remember which games were suggested
        game = data['ontology'][tourney][-1]

        typeOfMatch = game['week']
        vars[team1] = game['teams'][0]
        vars[team2] = game['teams'][1]
        vars[winner] = game['winner']
        date = game['time'][0:10]
        month = date[5:7]
        day = date[-2:]

        # playoffs
        if typeOfMatch[0:8] == 'Playoffs':
            vars[t_typeOfMatch] = typeOfMatch[-7:].lower() + " " + typeOfMatch[0:8].lower()
        # knockout or weekly games
        else:
            vars[t_typeOfMatch] = typeOfMatch.lower()

        # change numerical month to month name
        if month == '01':
            vars[t_month] = 'January'
        elif month == '02':
            vars[t_month] = 'February'
        elif month == '03':
            vars[t_month] = 'March'
        elif month == '04':
            vars[t_month] = 'April'

        # rd, st, th for days
        if day[-1:] == '2' or day[-1:] == '3':
            vars[t_day] = day + "rd"
        elif day[-1:] == 1:
            vars[t_day] = day + "st"
        else:
            vars[t_day] = day + "th"

        return True


class UserInputChampion(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):

        # variables
        playerRec = 'PLAYER_RECOMMEND'
        fav_champ = 'FAV_CHAMP'

        # opening jason
        f = open('resources/champs.json', )
        data = json.load(f)
        # takes user input as string
        mystr = ngrams.text()

        # loads spacy model to tokenize string
        nlp = spacy.load("en_core_web_md")
        doc = nlp(mystr)

        # turns user input into a list of strings
        sentenceSplit = mystr.split()

        # top, mid, jungle, bot, support
        for role in data['ontology']['lane']:
            # iterates through each champion
            for champion in data['ontology'][role]:
                # for each token in user's sentence
                for token in doc:
                    # champions are labeled as nouns by spacy
                    if token.pos_ == 'NOUN':
                        # if champion in ontology and player suggested champion is same as champion in iteration
                        if token.text in data['ontology'] and champion == token.text:
                            # keeps track of first player in ont who plays that champion in lcs
                            # TODO keep track of recommended players
                            # TODO handle cases where user does not have favorite champ
                            # TODO handle cases where user misspells champion
                            # TODO handle cases where user has multiple favorite champions
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
        randomNum = random.randint(0, 1)
        if randomNum == 1:
            print('yes')
            return True
        else:
            return False


class MacroGPTJSON(Macro):
    def __init__(self, request: str, full_ex: Dict[str, Any], empty_ex: Dict[str, Any] = None,
                 set_variables: Callable[[Dict[str, Any], Dict[str, Any]], None] = None) -> object:
        """
        :rtype: object
        :param request: the task to be requested regarding the user input (e.g., How does the speaker want to be called?).
        :param full_ex: the example output where all values are filled (e.g., {"call_names": ["Mike", "Michael"]}).
        :param empty_ex: the example output where all collections are empty (e.g., {"call_names": []}).
        :param set_variables: it is a function that takes the STDM variable dictionary and the JSON output dictionary and sets necessary variables.
        """
        self.request = request
        self.full_ex = json.dumps(full_ex)
        self.empty_ex = '' if empty_ex is None else json.dumps(empty_ex)
        self.check = re.compile(regexutils.generate(full_ex))
        self.set_variables = set_variables

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        examples = f'{self.full_ex} or {self.empty_ex} if unavailable' if self.empty_ex else self.full_ex
        prompt = f'{self.request} Respond in the JSON schema such as {examples}: {ngrams.raw_text().strip()}'
        output = gpt_completion(prompt)
        if not output: return False

        try:
            print(output)
            d = json.loads(output)
        except JSONDecodeError:
            print(f'Invalid: {output}')
            return False

        if self.set_variables:
            self.set_variables(vars, d)
        else:
            vars.update(d)

        return True


class MacroNLG(Macro):
    def __init__(self, generate: Callable[[Dict[str, Any]], str]):
        self.generate = generate

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        return self.generate(vars)


def gpt_completion(input: str, regex: Pattern = None) -> str:
    response = openai.ChatCompletion.create(
        model=CHATGPT_MODEL,
        messages=[{'role': 'user', 'content': input}]
    )
    output = response['choices'][0]['message']['content'].strip()

    if regex is not None:
        m = regex.search(output)
        output = m.group().strip() if m else None

    return output


# Section: casual communication: What's your favorite game?

def getFavGame(vars: Dict[str, Any]):
    return vars['GameType']


def getReason(vars: Dict[str, Any]):
    return vars['WhyInterest']


def getActivityWithFriends(vars: Dict[str, Any]):
    return vars['WithFriendActivities']


# Section: some fundamental macros to get attitude/sentiment... from users
def PositiveAgreement(vars: Dict[str, Any]):
    if vars['Agreement'] == 'yes':
        return True
    else:
        return False

def NegativeAgreement(vars: Dict[str, Any]):
    if vars['Agreement'] == 'no':
        return True
    else:
        return False
