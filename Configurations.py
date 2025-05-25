'''

@author Maurice Amon
'''
from itertools import product

from techniques.PromptType import PromptType

'''
Configuration-singleton for all parameters that need to be set before executing the tests.
'''


class Configurations():

    # List of all the parameters with their set of values ..
    _temperatures_range = (0, 0.2, 0.4, 0.5)
    # List of all the values for top p ..
    _top_p_range = (0.8, 0.9, 0.95, 1)
    # List of all values for top k parameter ..
    _top_k_range = (1, 40, 100)
    # Fixed value for temperature ..
    _temperature_fixed = 0
    # Fixed value for top p ..
    _top_p_fixed = 1
    # Fixed value for top k ..
    _top_k_fixed = 1
    # List of all values for context length ..
    _context_length = (1024, 2048)
    # How much should a repetition get "punished"? [1.1; 1.5] : strong punishment; [1.6; infinity] Very strong punishment
    _repeat_penalty = 1.4
    # seed
    _seed = 128
    # Max tokens ..
    _max_tokens = 256

    #_prompt_scenarios = [PromptType.ZERO_SHOT, PromptType.FEW_SHOT, PromptType.META, PromptType.GEN_META, PromptType.CoT]
    _prompt_scenarios = [PromptType.CoT]



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configurations, cls).__new__(cls)
        return cls.instance

    def get_cartesian_product(self):
        parameter_sets = [self._temperatures_range, self._top_p_range, self._top_k_range]
        return list(product(*parameter_sets))

    def get_prompt_scenarios(self):
        return self._prompt_scenarios

    def get_context_length(self):
        return self._context_length

    def get_repeat_penalty(self):
        return self._repeat_penalty

    def get_seed(self):
        return self._seed

    def get_max_tokens(self):
        return self._max_tokens

    def set_top_p_fixed(self, top_p):
        self._top_p_fixed = top_p


    def get_top_p_fixed(self):
        return self._top_p_fixed

    def get_top_k_fixed(self):
        return self._top_k_fixed

    def set_temperature(self, temperature):
        self._temperature_fixed = temperature

    def get_temperature_fixed(self):
        return self._temperature_fixed


