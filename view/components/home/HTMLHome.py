'''

@author Maurice Amon
'''
from abc import ABC


class HTMLHome(ABC):

    _home = ""

    def get_home(self) -> str:
        return self._home