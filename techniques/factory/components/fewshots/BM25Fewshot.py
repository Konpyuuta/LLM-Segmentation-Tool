'''

@author Maurice Amon
'''
from techniques.factory.components.fewshots.Fewshot import Fewshot


class BM25FewShot(Fewshot):

    _example = '''ENTER A FEW EXAMPLES FOR SEGMENTATION'''

    _source_code = '''SOURCE-CODE: '''

    _prompt = f'''PROMPT: Create a semantical segmentation of the SOURCE-CODE above with using ### as a delimiter.'''

    _few_shot = ''''''

    def __init__(self, **kwargs):
        self.initialize_fewshot()

    def initialize_fewshot(self):
        self._few_shot = f'''{self._example}\n\n{self._source_code}\n\n{self._prompt}'''

    def get_prompt(self):
        return self._few_shot

