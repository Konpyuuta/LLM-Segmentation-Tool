'''

@author Maurice Amon
'''
from techniques.PromptType import PromptType
from techniques.factory.BSIPasswordFactory import BSIPasswordFactory
from techniques.factory.CriteriaSelectionFactory import CriteriaSelectionFactory
from techniques.factory.ExampleCompanyScenarioFactory import ExampleCompanyScenarioFactory
from techniques.factory.FullCriteriaSelectionFactory import FullCriteriaSelectionFactory
from techniques.factory.PlaybookFactory import PlaybookFactory
from techniques.factory.SecAdviceFactory import SecAdviceFactory
from techniques.factory.scenarios.BSIPasswordScenario import BSIPasswordScenario
from techniques.factory.scenarios.CriteriaSelectionScenario import CriteriaSelectionScenario
from techniques.factory.scenarios.ExampleCompanyScenario import ExampleCompanyScenario
from techniques.factory.scenarios.FullCriteriaSelectionScenario import FullCriteriaSelectionScenario
from techniques.factory.scenarios.PlaybookScenario import PlaybookScenario
from techniques.factory.scenarios.SecAdviceScenario import SecAdviceScenario


class PromptClient():

    _factory = CriteriaSelectionFactory()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PromptClient, cls).__new__(cls)
        return cls.instance


    def create_prompt_comparison(self, type: PromptType):
        scenario = None
        match type:
            case PromptType.LAPTOP_PLAYBOOK:
                self._factory = PlaybookFactory()
                scenario = PlaybookScenario(self._factory)
            case PromptType.BSI_PASSWORD_LENGTH:
                self._factory = BSIPasswordFactory()
                scenario = BSIPasswordScenario(self._factory)
            case PromptType.CRITERIA_SELECTION:
                self._factory = CriteriaSelectionFactory()
                scenario = CriteriaSelectionScenario(self._factory)
            case PromptType.SEC_ADVICE:
                self._factory = SecAdviceFactory()
                scenario = SecAdviceScenario(self._factory)
            case PromptType.FULL_CRITERIA_SELECTION:
                self._factory = FullCriteriaSelectionFactory()
                scenario = FullCriteriaSelectionScenario(self._factory)
            case PromptType.EXAMPLE_COMPANY:
                self._factory = ExampleCompanyScenarioFactory()
                scenario = ExampleCompanyScenario(self._factory)

        scenario.initialize_techniques()
        return scenario