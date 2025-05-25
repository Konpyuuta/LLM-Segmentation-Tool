'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass
