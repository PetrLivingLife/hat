from base.basetest import BaseTest
from selenium.webdriver.common.by import By

#######
from time import sleep
from selenium.webdriver.common.keys import Keys
#######

# class Login(BaseTest):
#
#     def test_valid_login(self):
#         self.app.login_screen.login("petr", "heslo")
#         pass


class TestSearchSeznam(BaseTest):

    def test_simple_search(self):
        self.app.go_to_url("https://seznam.cz")
        search = self.app.app_driver.find_element(By.CSS_SELECTOR, 'div.search-form input[name=q].input')
        search.send_keys("hele")
        search.send_keys(Keys.ENTER)
        sleep(3)
