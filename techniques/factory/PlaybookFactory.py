'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.autocot.PlaybookAutoCoT import PlaybookAutoCoT
from techniques.factory.components.cot.PlaybookCoT import PlaybookCoT
from techniques.factory.components.fewshots.PlaybookFewshot import PlaybookFewshot
from techniques.factory.components.meta.PlaybookMeta import PlaybookMeta
from techniques.factory.components.zeroshot.PlaybookZeroshot import PlaybookZeroshot


class PlaybookFactory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return PlaybookZeroshot()

    def create_few_shots(self):
        return PlaybookFewshot()

    def create_cot_instruction(self):
        return PlaybookCoT()

    def create_auto_cot_instruction(self):
        return PlaybookAutoCoT()

    def create_meta_instruction(self):
        return PlaybookMeta()