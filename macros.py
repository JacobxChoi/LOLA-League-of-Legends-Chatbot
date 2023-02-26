from emora_stdm import Macro, Ngrams
from typing import Dict, Any, List

class MacroEsportsOrLeague(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        return True