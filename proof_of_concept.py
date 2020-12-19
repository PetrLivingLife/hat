# NOT WORKING, trying out
from selenium.webdriver import Chrome as Chrome_, Firefox as Firefox_
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# from appium import webdriver as appium_driver

from unittest import TestCase
from unittest import main as unittest_main


class Chrome(Chrome_):
    def __init__(self):
        super().__init__(ChromeDriverManager().install())


class Firefox(Firefox_):
    def __init__(self):
        super().__init__(executable_path=GeckoDriverManager().install())


class Android(object):
    pass


class Ios(object):
    pass


class Locator(object):

    def __init__(self, path_type, path):
        self.path_type = path_type
        self.path = path

    def __get__(self, instance, owner):
        # TODO Resolve why this is never called -> need to unpack those manually
        #   might be something with metaclasses, plus this not being on actual instance... - probably not worth it
        #   using __call and locator() instead for now
        return self.path_type, self.path

    def __call__(self):
        return self.path_type, self.path


class AppElement(object):

    def __init__(self,
                 browser_locator: Locator = None,
                 android_locator: Locator = None,
                 ):
        self.browser = browser_locator
        self.android = android_locator

    def __get__(self, instance, owner):
        # TODO move this elsewhere, keeping the mapping working
        locators_resolution = {
            Chrome: self.browser,
            Firefox: self.browser,
            Android: self.android,
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


class HomePage(BaseScreen):
    # seznam.cz
    search_field = AppElement(browser_locator=Locator(By.CSS_SELECTOR, 'div.search-form input[name=q].input'))

    def search(self, search_term):
        self.search_field.send_keys(search_term)


class LoginScreen(BaseScreen):
    # TODO Rethink how to handle locators
    username_field = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "input.username"),
                                android_locator=Locator("CSS", "com.input.username"),)
    password_field = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "input.password"),
                                android_locator=Locator("CSS", "com.input.password"),)

    def login(self, username, password):
        # self.username_field.send_keys(username)
        # self.password_field.send_keys(password)
        print(self.username_field.path)


class App(object):

    def __init__(self, app_driver):
        self.app_driver = app_driver
        self.home_screen = HomePage(self.app_driver)
        self.login_screen = LoginScreen(self.app_driver)

        # Add shortcuts
        self.quit = self.app_driver.quit.__get__(self, self.__class__)
        self.go_to = self.app_driver.get.__get__(self, self.__class__)


class BaseTest(TestCase):
    def setUp(self) -> None:
        # self.app = App(Chrome())
        self.app = App(Firefox())
        self.app.go_to("https://seznam.cz")

    def tearDown(self) -> None:
        self.app.quit()


# class TestLogin(BaseTest):
#
#     def test_valid_login(self):
#         self.app.login_screen.login("valid", "login")


class TestSearch(BaseTest):
    def test_simple_search(self):
        self.app.home_screen.search("hele")


if __name__ == '__main__':
    unittest_main()
