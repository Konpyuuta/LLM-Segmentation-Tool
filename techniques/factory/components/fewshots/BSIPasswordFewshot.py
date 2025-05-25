'''

@author Maurice Amon
'''
from techniques.factory.components.fewshots.Fewshot import Fewshot


class BSIPasswordFewshot(Fewshot):

    _example = '''
Question: How many hours a day does my friend at minimum spend at work?
          Just output the number for the minimal hours, omit everything else.

Response: 10

Question: How many hours of sleep does a human minimally need at night?
          Just output the number for the minimal hours of sleep, omit everything else.

Response: 7'''

    _prompt = '''
Question: Which minimal password length does the "Bundesamt für Sicherheit in der Informationstechnik" (BSI) recommend?
          Just output the number for the minimal password length, omit everything else.'''

    _few_shot = ''''''

    def __init__(self, **kwargs):
        self.initialize_fewshot()

    def initialize_fewshot(self):
        self._few_shot = f'''{self._example}\n\n{self._prompt}'''


    def get_prompt(self):
        return self._few_shot