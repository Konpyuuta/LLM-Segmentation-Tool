'''
@author: Maurice Amon
'''
from view.components.about.HTMLAbout import HTMLAbout


class HTMLStandardAbout(HTMLAbout):

   def __init__(self):
      super(HTMLStandardAbout, self).__init__()
      self.initializeContent()


   # Implementing abstract method ..
   def initializeContent(self):
      self._content = '''<h1 class=\"text-center\">'''
      self._content += 'About'
      self._content += '''</h1><div class=\"container py-5 bg-light\" style=\"border-radius: 15px;\">This applications has been developed to automate the tests for the M. Sc. Seminar in Software Engineering.</div>'''

   def getContent(self) -> str:
      return self._content