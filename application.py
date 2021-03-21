import logging
from abc import ABC, abstractmethod


log = logging.getLogger(__name__)


class AbstractAppUi(ABC):
    """Represents and contains all screens, their elements and possible actions.

    Any screen you want to use in tests, should be instanced within _setup method.
    It gets automatically called when AppUi is initialized before test.
    e.g.
      self.home_screen = HomeScreen(self.platform_driver)
    """

    def __init__(self,
                 platform_driver,
                 ):
        self.platform_driver = platform_driver
        self._setup()

    @abstractmethod
    def _setup(self,):
        pass


class BaseScreen(object):
    def __init__(
                 self,
                 platform_driver,
                 ):
        # Platform driver is needed here, so that later .get_element methods can call it.
        self.platform_driver = platform_driver


class AppElement(object):
    """Class to hold all information needed to use application elements in tests.

    Parameters:
    locator_dictionary: dictionary with {'platform/locator type': 'locator'} items.
        This is mainly useful if you want to use custom driver and none of existing attributes suites that.
        Locator type (key) has to have same value as .locator_type attribute of your driver.
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
                instance: BaseScreen,
                owner,
                ):
        # Leave the platform resolution to Driver().
        return instance.platform_driver.get_element(self)

    def __str__(self):
        return str({"AppElement": self.__dict__})

    def __repr__(self):
        return self.__str__()

    def _add_locators_from_locator_dict(self):
        if self.locator_dictionary:
            for locator_type, locator in self.locator_dictionary.items():
                setattr(self, locator_type, locator)

    def is_displayed(self):
        # I haven't found a way yet to make this working as I need the instance also here,
        #  or some other way to access the driver etc
        if self is None:
            return False
