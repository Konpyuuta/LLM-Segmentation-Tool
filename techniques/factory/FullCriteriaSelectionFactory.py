'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.cot.FullCriteriaSelectionCoT import FullCriteriaSelectionCoT
from techniques.factory.components.fewshots.FullCriteriaSelectionFewshot import FullCriteriaSelectionFewShot
from techniques.factory.components.zeroshot.FullCriteriaSelectionZeroshot import FullCriteriaSelectionZeroshot


class FullCriteriaSelectionFactory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return FullCriteriaSelectionZeroshot()

    def create_few_shots(self):
        return FullCriteriaSelectionFewShot()

    def create_cot_instruction(self):
        return FullCriteriaSelectionCoT()

    def create_auto_cot_instruction(self):
        pass

    def create_meta_instruction(self):
        pass