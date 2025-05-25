'''

@author Maurice Amon
'''
from ProjectConstants import CURRENT_YEAR, PROJECT_AUTHOR
from view.components.footer.HTMLFooter import HTMLFooter


class HTMLStandardFooter(HTMLFooter):

    def __init__(self):
        super(HTMLStandardFooter, self).__init__()
        self.initialize()


    def initialize(self):
        self._footer += f'''\n
        <div class=\"container\">\n
        <footer class=\"py-3 my-4\">\n
        <ul class=\"nav justify-content-center border-bottom pb-3 mb-3\">\n
        <li class=\"nav-item\"><a href=\"/\" class=\"nav-link px-2 text-muted\">Home</a></li>\n
        <li class=\"nav-item\"><a href=\"/about\" class=\"nav-link px-2 text-muted\">About</a></li>\n
        </ul>\n
        <p class=\"text-center text-muted\">&copy; {CURRENT_YEAR} | {PROJECT_AUTHOR} | Software Engineering Group (SEG) @ University of Bern</p>\n
        </footer>\n
        </div>\n
        \n
        <div class=\"b-example-divider\"></div>'''

