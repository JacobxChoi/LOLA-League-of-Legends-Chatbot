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

class lolasFavChamp(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        r = re.compile(r"\s*([Jj]ojpyun)\s*")
        # m = r.search(ngrams.text())
        favChamp = False
        for m in re.finditer(r, ngrams.text()):
            if m.group(1) is not None:
                favChamp = True
        return favChamp

class MacroRandNum(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        randomNum = random.randint(0,1)
        if randomNum==1:
            print('yes')
            return True
        else:
            return False