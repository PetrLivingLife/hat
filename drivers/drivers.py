import logging
from abc import ABC, abstractmethod

from application import AppElement

# TODO Watch for circular imports, these are used for type hinting
# from application import AppUi
# from drivers import BaseCustomDriver
# from hat import Hat


log = logging.getLogger(__name__)


class BaseCustomDriver(ABC):
    """Basic/abstract implementation with all methods that should every driver support.

    When implementing custom driver, you should inherit from this class and implement needed methods.
    You should implement (overwrite) methods only with underscore, e.g. _start()
        as start() etc. is exposed to test and its behaviour shouldn't alter between platforms.
    You will get warning messages in logs in case a method is missing its implementation.
    You should also set all needed attributes per driver implementation.

    Attributes:

    platform_type : str
        Identifies what attribute to select from AppElement by its name. e.g. 'browser', 'android', 'ios'

    name : str
        String by which drivers are resolved to be used for tests.
    """

    # TODO implement these as abstract as well if possible
    name: str
    platform_type: str

    def __init__(self,
                 ):
        self.platform_type = self.platform_type
        self.name = self.name
        self.platform_driver = None

    def start(self, headless=False, *args, **kwargs):
        log.info(f"Starting platform and driver: {self.platform_type, self.name}")
        # run method returned by _start() and pass arguments to it
        self.platform_driver = self._start(headless=headless, *args, **kwargs)
        return self

    @abstractmethod
    def _start(self,):
        pass

    def open_app(self, url):
        return self._open_app(url)

    @abstractmethod
    def _open_app(self,):
        pass

    def close(self,):
        log.info(f"Closing platform and driver.")
        return self._close()

    @abstractmethod
    def _close(self,):
        self.get_element()
        pass

    def get_element(self, app_element):  # -> AppElement:
        """
        Basic method to work with an application elements.

        Parameters:
            app_element (AppElement, string): AppElement is preffered.
                Though you can provide locators in whatever form your driver (implementation) supports.

        Returns:
            TODO AppElement: element to perform operations on.
        """
        log.debug(f"Looking for element: {app_element}")
        if isinstance(app_element, AppElement):
            return self._get_element(getattr(app_element, self.platform_type))
        # If called with just locator:
        return self._get_element(app_element)

    @abstractmethod
    def _get_element(self,):
        """Implement call to the platform driver method to find/obtain element

        e.g.:
        playwright:
            return self.tab.query_selector(locator)
        selenium:
            return self.driver.find_element(*processed_locator)

        You may need to process the locator, coming from self.get_element()
        You should also implement logic to always return (new instance of) AppElement even
        if the element is not present and set it with proper attributes like
            .is_present = False/True,
            .is_displayed = False/True
            ...
        """
        pass

    @abstractmethod
    def _remap_methods(self,):
        # TODO Rethink if this can be done better
        pass
