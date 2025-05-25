'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class AutoCoT(ABC):

    __auto_cot = None

    @abstractmethod
    def initialize_auto_cot(self):
        pass