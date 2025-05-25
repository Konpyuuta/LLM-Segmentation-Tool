'''

@author Maurice Amon
'''
from enum import Enum


class PromptType(Enum):

    ZERO_SHOT = 0,
    FEW_SHOT = 1,
    META = 2,
    GEN_META = 3,
    CoT = 4