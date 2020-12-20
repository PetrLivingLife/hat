from app_screens.home import HomeScreen
from app_screens.login import LoginScreen


class AppUi(object):

    def __init__(self, app_driver):
        self.app_driver = app_driver
        self.home_screen = HomeScreen(self.app_driver)
        self.login_screen = LoginScreen(self.app_driver)

        # Add shortcuts
        self.quit = self.app_driver.quit.__get__(self, self.__class__)
        self.go_to_url = self.app_driver.get.__get__(self, self.__class__)

    def go_to_home_screen(self):
        self.home_screen.home_button.click()
        # wait for load

    def go_to_login_screen(self):
        self.go_to_home_screen()
        self.home_screen.login_link.click()
        # wait for load
