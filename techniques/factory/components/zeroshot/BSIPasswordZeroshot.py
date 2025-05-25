'''

@author Maurice Amon
'''
from techniques.factory.components.zeroshot.Zeroshot import Zeroshot


class BSIPasswordZeroshot(Zeroshot):

    def __init__(self):
        self.initialize()

    def initialize(self):
         self._instruction = f'''Which minimal password length does the "Bundesamt für Sicherheit in der Informationstechnik" (BSI) recommend?
                                 Just output the number for the minimal password length, omit everything else.'''


    def get_prompt(self):
        return self._instruction