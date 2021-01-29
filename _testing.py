import logging

from os import path, getcwd

from configuration import configuration
from base.basetest import BaseTest


configuration.setup_logging()

################

from selenium.webdriver.common.by import By

#######
from time import sleep
from selenium.webdriver.common.keys import Keys
#######


class SearchSeznam(BaseTest):

    def test_simple_search(self):
        self.app.go_to_url("https://seznam.cz")
        search = self.app.app_driver.find_element(By.CSS_SELECTOR, 'div.search-form input[name=q].input')
        search.send_keys("hele")
        search.send_keys(Keys.ENTER)
        sleep(3)

from unittest import main

main()