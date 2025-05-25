'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class Meta(ABC):

    __meta_instruction = None

    @abstractmethod
    def initialize_meta_instruction(self):
        pass