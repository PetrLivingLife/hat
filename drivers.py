import logging
from abc import ABC, abstractmethod

from playwright.sync_api import sync_playwright

import application


log = logging.getLogger(__name__)


class Driver(ABC):
    """Abstract implementation with all methods that should every platform driver support.

    When implementing custom driver, you should inherit from this class and implement needed methods.
    You should implement methods only with underscore, e.g. _start()
        as open_app() etc. is exposed to test and its behaviour shouldn't alter between platforms.
    You will get warning messages in logs in case a method is missing its implementation.
    You should also set all needed attributes per driver implementation.

    Attributes:

    name : str
        String by which drivers are resolved to be used for tests.

    platform_type : str
        Identifies what attribute to select from AppElement by its name. e.g. 'browser', 'android', 'ios'

    """

    # TODO implement these as abstract as well if possible
    name: str
    platform_type: str

    def __init__(self,
                 headless: bool = False,
                 *args,
                 **kwargs,
                 ):
        self.platform_type = self.platform_type
        self.name = self.name
        log.info(f"Starting platform and driver: {self.platform_type, self.name}")
        self.platform_driver = self._start(headless=headless, *args, **kwargs)

    @abstractmethod
    def _start(self,):
        pass

    def open_app(self, url):
        return self._open_app(url)

    @abstractmethod
    def _open_app(self,):
        pass

    def close_app(self,):
        log.info(f"Closing application instance.")
        return self._close_app()

    @abstractmethod
    def _close_app(self,):
        pass

    def quit(self,):
        log.info(f"Closing platform.")
        return self._quit()

    @abstractmethod
    def _quit(self,):
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
        if isinstance(app_element, application.AppElement):
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


class Playwright(Driver):
    """Wrap around existing Playwright to customise it for running inside this framework.
    """
    platform_type = 'browser'

    def _open_app(self, url: str):
        # TODO Rewrite this with loading url from configuration
        self.application_instance = self.platform_driver.new_page()
        self.application_instance.goto(f"{url}")
        return self.application_instance

    def _close_app(self):
        self.platform_driver.close()

    def _quit(self):
        self.playwright.stop()

    def _get_element(self, locator):
        # TODO Either here or in BaseCustomDriver implement logic to return AppElement instead of 'NoneType'
        return self.application_instance.query_selector(locator)

    def _start(self, headless=False, locale='en-GB', **kwargs):
        self.playwright = sync_playwright().start()
        browser = self._get_specific_browser().launch(headless=headless)
        return browser.new_context(locale=locale)

    @abstractmethod
    def _get_specific_browser(self,):
        # To be implemented in browser specific class
        pass


class Chromium(Playwright):
    name = 'chromium'

    def _get_specific_browser(self):
        return self.playwright.chromium


class Firefox(Playwright):
    name = 'firefox'

    def _get_specific_browser(self):
        return self.playwright.firefox


class Webkit(Playwright):
    name = 'webkit'

    def _get_specific_browser(self):
        return self.playwright.webkit
