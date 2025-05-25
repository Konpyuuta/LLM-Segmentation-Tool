'''

@author Maurice Amon
'''
from abc import ABC


class PromptingTechnique(ABC):

    _prompt = None

    _prepared_prompt = None

    def __init__(self, _prompt):
        self._prompt = _prompt

    def prepare_prompt(self):
        raise NotImplementedError()

    def get_prompt(self):
        return self._prompt

    def get_prepared_prompt(self):
        return self._prepared_prompt
    