'''

@author Maurice Amon
'''
from abc import ABC, abstractmethod


class LLMConnector(ABC):

    @abstractmethod
    def initiate_connection(self):
        pass

    @abstractmethod
    def send_request(self, question: str):
        pass

    @abstractmethod
    def read_response(self) -> str:
        pass

    @abstractmethod
    def extract_response(self, response: str) -> str:
        pass

    @abstractmethod
    def get_response(self):
        pass