'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class Scenario(ABC):

    __technique_prompts = None

    def __init__(self):
        self.__technique_prompts = []

    @abstractmethod
    def initialize_techniques(self):
        pass

    @abstractmethod
    def get_technique_prompts(self):
        return self.__technique_prompts