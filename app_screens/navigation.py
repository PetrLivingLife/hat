
class Navigation(object):

    def __init__(self, app_driver):
        self.app_driver = app_driver

    def account_screen(self):
        self.app_driver.home_screen.account_link.click()
