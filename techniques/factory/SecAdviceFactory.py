'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.fewshots.SecAdviceFewshot import SecAdviceFewshot
from techniques.factory.components.zeroshot.SecAdviceZeroshot import SecAdviceZeroshot


class SecAdviceFactory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return SecAdviceZeroshot()

    def create_few_shots(self):
        return SecAdviceFewshot()

    def create_cot_instruction(self):
        pass

    def create_auto_cot_instruction(self):
        pass

    def create_meta_instruction(self):
        pass