'''

@author Maurice Amon
'''
from abc import ABC

from techniques.factory.components.meta.Meta import Meta


class PlaybookMeta(Meta):

    __meta_instruction = '''Let's think step by step:
                            1. *** Explain the next steps that need to be done immediately. ***
                            2. *** Assess the impact of the incident. ***
                            3. *** Estimation of the damage and legal actions. ***
                            4. *** Suggestions to prevent such incidents in the future. ***
                            5. *** Monitor for future threats. ***'''

    _prompt = '''Please write a playbook/incident-response for an employee in the following situation:
                The employee works as an assistant in a hospital where he's responsible for administrating the patients data. 
                While he was going to the office, he lost his laptop in the train. 
                The data of the patients were stored on this laptop together with other highly private data.'''

    _meta_prompt = None

    def __init__(self):
        super().__init__()
        self.initialize_meta_instruction()

    def initialize_meta_instruction(self):
        self._meta_prompt = f'''Problem statement: {self._prompt}
                                Solution structure: 
                                {self.__meta_instruction}
                            '''

    def get_prompt(self):
        return self._meta_prompt
