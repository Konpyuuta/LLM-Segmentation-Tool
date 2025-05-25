'''

@author: Maurice Amon
'''
from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class SecAdviceZeroshot(Zeroshot):

    def __init__(self):
        self.initialize()

    def initialize(self):
         self._instruction = f'''I run a company with 300 employees in a trade business. How many security would you recommend for my company?'''


    def get_prompt(self):
        return self._instruction