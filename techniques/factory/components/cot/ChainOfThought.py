'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class ChainOfThought(ABC):

    __cot = None

    @abstractmethod
    def initialize_cot(self):
        pass