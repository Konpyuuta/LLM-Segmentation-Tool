'''

@author Maurice Amon
'''
from techniques.factory.components.fewshots.Fewshot import Fewshot


class SecAdviceFewshot(Fewshot):
    
    _example = '''
                Question: How many hours does a workday include. 
                Response: The answer is 8 hours.'''

    _prompt = '''
                Question: I run a company with 300 employees in a trade business. How many security would you recommend for my company?'''

    _few_shot = ''''''

    def __init__(self, **kwargs):
        self.initialize_fewshot()

    def initialize_fewshot(self):
        self._few_shot = f'''{self._example}\n\n{self._prompt}'''


    def get_prompt(self):
        return self._few_shot