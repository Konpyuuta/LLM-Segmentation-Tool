'''

@author Maurice Amon
'''
from techniques.PromptingTechnique import PromptingTechnique


class ZeroshotTechnique(PromptingTechnique):

    def __init__(self, _prompt):
        super(ZeroshotTechnique, self).__init__(_prompt)

    def prepare_prompt(self):
        self._prepared_prompt = self._prompt