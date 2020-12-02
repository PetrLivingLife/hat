from .drivers import Chrome, Firefox, Android, Ios


class Locator(object):
    """
    locator_type: By.* selector type
    :path: str
    """

    def __init__(self,
                 locator_type,
                 path: str,
                 ):
        self.locator_type = locator_type
        self.path = path

    def __get__(self, instance, owner):
        # TODO Resolve why this is never called -> need to unpack those manually
        #   might be something with metaclasses, plus this not being on actual instance... - probably not worth it
        #   using __call__ and *locator() instead for now
        return self.locator_type, self.path

    def __call__(self):
        return self.locator_type, self.path


class AppElement(object):

    def __init__(self,
                 browser_locator: Locator = None,
                 android_locator: Locator = None,
                 ios_locator: Locator = None
                 ):
        self.browser_locator = browser_locator
        self.android_locator = android_locator
        self.ios_locator = ios_locator

    def __get__(self, instance, owner):
        # TODO move this mapping elsewhere, keeping the mapping working
        locators_resolution = {
            Chrome: self.browser_locator,
            Firefox: self.browser_locator,
            Android: self.android_locator,
            Ios: self.ios_locator,
        }
        # from instance - screen object, get driver type - Chrome, Firefox, Android...
        # via dictionary get proper locator
        locator = locators_resolution.get(instance.app_driver.__class__)
        # unpack the locator attributes for standard selenium find method and return the element
        return instance.app_driver.find_element(*locator())

    # def __set__(self, instance, value):
    #     pass


class BaseScreen(object):

    def __init__(self, app_driver):
        self.app_driver = app_driver
