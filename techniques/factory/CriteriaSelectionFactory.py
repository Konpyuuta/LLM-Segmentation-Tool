'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.fewshots.CriteriaSelectionFewshot import CriteriaSelectionFewshot
from techniques.factory.components.zeroshot.CriteriaSelectionZeroshot import CriteriaSelectionZeroshot


class CriteriaSelectionFactory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return CriteriaSelectionZeroshot()

    def create_few_shots(self):
        return CriteriaSelectionFewshot()

    def create_cot_instruction(self):
        pass

    def create_auto_cot_instruction(self):
        pass

    def create_meta_instruction(self):
        pass