from selenium.webdriver import Chrome as Chrome_, Firefox as Firefox_
from appium.webdriver import Remote as appium_driver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Chrome(Chrome_):
    def __init__(self):
        super(Chrome, self).__init__(ChromeDriverManager().install())


class Firefox(Firefox_):
    def __init__(self):
        super(Firefox, self).__init__(executable_path=GeckoDriverManager().install())


class Android(appium_driver):
    pass


class Ios(appium_driver):
    pass
