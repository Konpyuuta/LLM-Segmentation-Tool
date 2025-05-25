'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class HTMLNavigation(ABC):

    _navigation = ""

    def getNavigation(self) -> str:
        return self._navigation