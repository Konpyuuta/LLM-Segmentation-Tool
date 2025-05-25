'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.components.zeroshot.ExampleCompanyZeroshot import ExampleCompanyZeroshot


class ExampleCompanyScenarioFactory(ScenarioFactory):

    def __init__(self):
        pass

    def create_zero_shot(self):
        return ExampleCompanyZeroshot()

    def create_few_shots(self):
        pass

    def create_cot_instruction(self):
        pass

    def create_auto_cot_instruction(self):
        pass

    def create_meta_instruction(self):
        pass