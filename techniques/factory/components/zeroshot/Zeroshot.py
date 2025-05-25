'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class Zeroshot(ABC):

    _instruction = None

    _prompt = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass


