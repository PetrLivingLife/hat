import logging

from os import path, getcwd

from configuration import configuration
from base.basetest import BaseTest


configuration.setup_logging(
    # log_config_filepath="h",
    # logs_output_path=path.join(getcwd(), "logs"),
    # logging_level=logging.DEBUG,
)

log = logging.getLogger(__name__)

# log.debug("logger debug msg here")
# log.info("logger info msg here")
# log.warning("logger warning msg here")
# log.error("logger error msg here")
# log.critical("logger critical msg here")

################

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


class SearchSeznam(BaseTest):

    def test_simple_search(self):
        self.app.go_to_url("https://seznam.cz")
        search = self.app.app_driver.find_element(By.CSS_SELECTOR, 'div.search-form input[name=q].input')
        search.send_keys("hele")
        search.send_keys(Keys.ENTER)
        sleep(3)

from unittest import main

main()