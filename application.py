import logging
from abc import ABC, abstractmethod

import drivers


log = logging.getLogger(__name__)


class Application(ABC):
    """Represents and contains all screens, their elements and possible actions.

    Any screen you want to use in tests, should be instanced within _setup method.
    It gets automatically called when AppUi is initialized before test.
    e.g.
      self.home_screen = HomeScreen(self.driver)
    """

    def __init__(self,
                 driver: drivers.Driver,
                 ):
        self.driver = driver
        self._setup()

    @abstractmethod
    def _setup(self,):
        pass


class Screen(object):
    def __init__(
                 self,
                 driver: drivers.Driver,
                 ):
        # Platform driver is needed here, so that later .get_element methods can call it.
        self._driver = driver


class AppElement(object):
    """Class to hold all information needed to use application elements in tests.

    Parameters:
    locator_dictionary: dictionary with {'platform/locator type': 'locator'} items.
        This is mainly useful if you want to use custom driver and none of existing attributes suites that.
        Locator type (key) has to have same value as .platform_type attribute of your driver.
    """

    def __init__(self,
                 browser=None,
                 android=None,
                 ios=None,
                 locator_dictionary: dict = None,
                 ):
        self.browser = browser
        self.android = android
        self.ios = ios
        self.locator_dictionary = locator_dictionary
        self._add_locators_from_locator_dict()

    def __get__(
                self,
                instance: Screen,
                owner,
                ):
        # Leave the platform resolution to Driver().
        return instance._driver.get_element(self)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    def _add_locators_from_locator_dict(self):
        if self.locator_dictionary:
            for platform_type, locator in self.locator_dictionary.items():
                setattr(self, platform_type, locator)

    def is_displayed(self):
        # I haven't found a way yet to make this working as I need the instance also here,
        #  or some other way to access the driver etc
        if self is None:
            return False
