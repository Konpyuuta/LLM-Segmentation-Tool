'''

@author Maurice Amon
'''
from view.GuiFactory import GuiFactory
from view.components.about.HTMLAbout import HTMLAbout
from view.components.about.HTMLStandardAbout import HTMLStandardAbout
from view.components.footer.HTMLFooter import HTMLFooter
from view.components.footer.HTMLStandardFooter import HTMLStandardFooter

from view.components.header.HTMLStandardHeader import HTMLStandardHeader
from view.components.header.HTMLHeader import HTMLHeader
from view.components.home.HTMLHome import HTMLHome
from view.components.home.HTMLStandardHome import HTMLStandardHome

from view.components.navigation import HTMLNavigation
from view.components.navigation.HTMLStandardNavigation import HTMLStandardNavigation



class StandardStyleFactory(GuiFactory):

    def create_html_header(self) -> HTMLHeader:
        return HTMLStandardHeader()

    def create_html_navigation(self) -> HTMLNavigation:
        return HTMLStandardNavigation()

    def create_html_about(self) -> HTMLAbout:
        return HTMLStandardAbout()

    def create_home(self) -> HTMLHome:
        return HTMLStandardHome()

    def create_html_footer(self) -> HTMLFooter:
        return HTMLStandardFooter()