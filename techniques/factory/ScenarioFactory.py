'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class ScenarioFactory(ABC):

    # Adds a few shots to the prompt ..
    @abstractmethod
    def create_few_shots(self):
        pass

    # Adds zero-shot to the prompt ..
    @abstractmethod
    def create_zero_shot(self):
        pass

    @abstractmethod
    def create_meta_instruction(self):
        pass

    @abstractmethod
    def create_cot_instruction(self):
        pass

    @abstractmethod
    def create_auto_cot_instruction(self):
        pass



