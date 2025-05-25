'''

@author Maurice Amon
'''
from pathlib import Path
import sys, os.path

from _socket import gethostname

from model import CurrentWebpage
from view.Webpage import Webpage
from view.components.navigation.HTMLNavigation import HTMLNavigation



class HTMLStandardNavigation(HTMLNavigation):
    def __init__(self):
        super(HTMLStandardNavigation, self).__init__()
        self.generateNavigation()


    def generateNavigation(self):
        self._navigation = f'''<div class=\"container py-5\"><nav class=\"navbar navbar-expand-lg navbar-light bg-light\">\n
                <div class=\"container-fluid\">\n
                <a class=\"navbar-brand\" href=\"#\">
                <img src=\"'''
        self._navigation += ""
        self._navigation += '''http://localhost:8000/static/unibe.png\" height=\"80\" alt=\"Unibe Logo\" class=\"rounded-pill\">
                </a>\n<button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n
                <span class=\"navbar-toggler-icon\"></span>\n
                </button><span style="font-size: 32px;">M. Sc. Seminar in Software Engineering</span>\n
                <div class=\"collapse navbar-collapse\" id=\"navbarSupportedContent\">\n
                <ul class=\"navbar-nav me-auto mb-2 mb-lg-0\">\n
                <li class=\"nav-item\">\n
                <a class=\"nav-link '''
        if CurrentWebpage.current_webpage == Webpage.HOME_PAGE:
            self._navigation += '''active\" aria-current=\"page\"'''
        else:
            self._navigation += '''\"'''
        self._navigation += '''
                </div>\n
                </div>\n
                </nav></div>'''
