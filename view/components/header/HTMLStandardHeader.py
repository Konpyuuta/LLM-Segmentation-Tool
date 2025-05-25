'''
@author: Maurice Amon
'''
from ProjectConstants import CHAR_SET, CSS_STYLE_PATH, BOOTSTRAP_JAVASCRIPT_DEPENDENCY, MAIN_PAGE_TITLE, \
    BOOTSTRAP_CSS_DEPENDENCY
from view.components.header.HTMLHeader import HTMLHeader


class HTMLStandardHeader(HTMLHeader):

    def __init__(self):
        super(HTMLStandardHeader, self).__init__()
        self._header += '<head>\n'
        self.addCharset()
        self.addDependencies()
        self.addTitle()
        self._header += '</head>\n'


    def addCharset(self):
        self._header += f'<meta charset=" + "\"" + {CHAR_SET} + "\">\n'


    def addDependencies(self):
        self._header += f'''
        <script src="https://code.jquery.com/jquery-3.6.1.slim.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src=\"{BOOTSTRAP_JAVASCRIPT_DEPENDENCY}\"
        integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n
        <link rel=\"stylesheet\" href=\"{BOOTSTRAP_CSS_DEPENDENCY}\"
        integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n
        <link th:href=\"{CSS_STYLE_PATH}\" rel=\"stylesheet\" type=\"text/css\">\n
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
        <link rel=\"icon\" href=\"https://www.zhaw.ch/favicon.ico\" type=\"image/png\">'''


    def addTitle(self):
        self._header += f'''<title>{MAIN_PAGE_TITLE}</title>'''


