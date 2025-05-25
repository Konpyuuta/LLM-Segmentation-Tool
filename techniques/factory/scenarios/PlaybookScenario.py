'''

@author Maurice Amon
'''
from techniques.factory.ScenarioFactory import ScenarioFactory
from techniques.factory.scenarios.Scenario import Scenario


class PlaybookScenario(Scenario):

    _factory = None

    _zeroshot_prompt = None

    _fewshot_prompt = None

    _meta_prompt = None

    __technique_prompts = None

    def __init__(self, _factory: ScenarioFactory):
        super(PlaybookScenario, self).__init__()
        self._factory = _factory
        self.__technique_prompts = []

    def initialize_techniques(self):
        self._zeroshot_prompt = self._factory.create_zero_shot()
        self._fewshot_prompt = self._factory.create_few_shots()
        self._meta_prompt = self._factory.create_meta_instruction()
        self.__technique_prompts.append(self._zeroshot_prompt)
        self.__technique_prompts.append(self._fewshot_prompt)
        self.__technique_prompts.append(self._meta_prompt)


    def get_technique_prompts(self):
        return self.__technique_prompts
