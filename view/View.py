'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class View(ABC):

    _view = ""

    @abstractmethod
    def initialize_components(self):
        pass

    @abstractmethod
    def prepare_view(self):
        pass

    @abstractmethod
    def get_view_content(self) -> str:
        pass
