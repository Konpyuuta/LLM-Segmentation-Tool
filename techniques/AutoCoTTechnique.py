'''

@author Maurice Amon
'''
from techniques.PromptingTechnique import PromptingTechnique


class AutoCoTTechnique(PromptingTechnique):

    first_thought = None

    second_thought = None

    third_thought = None

    def __init__(self, _prompt):
        super(AutoCoTTechnique, self).__init__(_prompt)

    def prepare_prompt(self):
        self._prepared_prompt = f''''''