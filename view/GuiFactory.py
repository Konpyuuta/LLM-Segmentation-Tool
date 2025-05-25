from __future__ import annotations
from abc import ABC, abstractmethod

from view.components.about.HTMLAbout import HTMLAbout
from view.components.footer.HTMLFooter import HTMLFooter
from view.components.header.HTMLHeader import HTMLHeader

from view.components.home.HTMLHome import HTMLHome
from view.components.navigation import HTMLNavigation



class GuiFactory(ABC):

    @abstractmethod
    def create_html_header(self) -> HTMLHeader:
        pass

    @abstractmethod
    def create_html_navigation(self) -> HTMLNavigation:
        pass

    @abstractmethod
    def create_html_about(self) -> HTMLAbout:
        pass

    @abstractmethod
    def create_home(self) -> HTMLHome:
        pass

    @abstractmethod
    def create_html_footer(self) -> HTMLFooter:
        pass