'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.fewshots.BSIPasswordFewshot import BSIPasswordFewshot
from techniques.factory.components.zeroshot.BSIPasswordZeroshot import BSIPasswordZeroshot


class BM25Factory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return BSIPasswordZeroshot()

    def create_few_shots(self):
        return BSIPasswordFewshot()

    def create_cot_instruction(self):
        pass

    def create_auto_cot_instruction(self):
        pass

    def create_meta_instruction(self):
        pass