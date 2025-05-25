
'''
@author Maurice Amon

'''
from abc import ABC, abstractmethod


class HTMLHeader(ABC):

   _header = ""

   @abstractmethod
   def addCharset(self):
      pass

   @abstractmethod
   def addDependencies(self):
      pass

   @abstractmethod
   def addTitle(self):
      pass

   def getHeader(self) -> str:
      return self._header


