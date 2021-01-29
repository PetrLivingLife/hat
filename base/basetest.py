from .drivers import Chrome, Firefox, Android, Ios
from .app_ui import AppUi

import logging

from configuration import configuration as cfg


class BaseTest(object):
    
    def setup_method(self):
        log = logging.getLogger(__name__)
        log.info(f"Test case setup")
        self.app = AppUi(Firefox())
    
    def teardown_method(self):
        log = logging.getLogger(__name__)
        log.info(f"Cleaning after test.")
        log.info(f"Closing application.")
        self.app.quit()
