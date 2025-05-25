'''

@author Maurice Amon
'''
from dis import Instruction

from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class PlaybookZeroshot(Zeroshot):

    def __init__(self):
        self.initialize()

    def initialize(self):
         self._instruction = f'''Please write a playbook/incident-response for an employee in the following situation:
         The employee works as an assistant in a hospital where he's responsible for administrating the patients data. 
         While he was going to the office, he lost his laptop in the train. 
         The data of the patients were stored on this laptop together with other highly private data.'''


    def get_prompt(self):
        return self._instruction
