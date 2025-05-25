'''

@author Maurice Amon
'''
from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class BM25Zeroshot(Zeroshot):

    _source_code = None

    def __init__(self):
        self.initialize()

    def initialize(self):
         self._instruction = f'''¨SOURCE CODE: {self._source_code}
                                 PROMPT: Create a semantical segmentation of the SOURCE CODE above with using ### as a delimiter. '''


    def get_prompt(self):
        return self._instruction