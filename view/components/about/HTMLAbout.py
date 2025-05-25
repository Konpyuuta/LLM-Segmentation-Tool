
'''
@author Maurice Amon

'''
from abc import ABC, abstractmethod


class HTMLAbout(ABC):

   _content = ""

   @abstractmethod
   def initializeContent(self):
      pass

   def getContent(self) -> str:
      return self._content