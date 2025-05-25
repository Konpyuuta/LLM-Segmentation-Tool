'''
@author Maurice Amon

'''
from abc import ABC, abstractmethod

class HTMLFooter(ABC):

   _footer = ""

   @abstractmethod
   def initialize(self):
      pass


   def getFooter(self) -> str:
      return self._footer

