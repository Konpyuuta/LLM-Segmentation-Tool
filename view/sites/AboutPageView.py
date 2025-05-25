'''

@author Maurice Amon
'''
from view.GuiFactory import GuiFactory
from view.View import View


class AboutPageView(View):

    __factory = None

    __header = None

    __navigation = None

    __about = None

    __footer = None

    def __init__(self, factory: GuiFactory):
        super(AboutPageView, self).__init__()
        self.__factory = factory

    def initialize_components(self):
        self.__header = self.__factory.create_html_header()
        self.__navigation = self.__factory.create_html_navigation()
        self.__about = self.__factory.create_html_about()
        self.__footer = self.__factory.create_html_footer()

    def prepare_view(self):
        self._view = '<!DOCTYPE html>\n<html lang=\"en\">\n'
        self._view += self.__header.getHeader()
        self._view += '<body>\n\n'
        self._view += self.__navigation.getNavigation()
        self._view += self.__about.getContent()
        self._view += self.__footer.getFooter()
        self._view += '</body>\n</html>'

    def get_view_content(self):
        return self._view