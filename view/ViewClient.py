'''
/** Singleton for accessing View-components ...
 *
 * @author Maurice Amon
 */
'''

from view import Webpage, View
from view.StandardStyleFactory import StandardStyleFactory
from view.sites.AboutPageView import AboutPageView
from view.sites.HomePageView import HomePageView



class ViewClient(object):


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ViewClient, cls).__new__(cls)
        return cls.instance

    def create_webpage(self, webpage:Webpage, data) -> View:
        view = None
        gui_factory = StandardStyleFactory()
        match webpage:
            case Webpage.Webpage.ABOUT_PAGE:
                view = AboutPageView(gui_factory)
            case Webpage.Webpage.HOME_PAGE:
                view = HomePageView(gui_factory)
            case _:
                view = "Something went wrong .."
        view.initialize_components()
        view.prepare_view()
        return view

