from .drivers import Chrome, Firefox, Android, Ios
from .app_ui import AppUi

from unittest import TestCase as _TestCase

import logging

from configuration import configuration as cfg


class BaseTest(_TestCase):


    def setUp(self) -> None:
        log = logging.getLogger(__name__)
        log.info(f"Test case setup")
        self.app = AppUi(Firefox())

    def tearDown(self) -> None:
        log = logging.getLogger(__name__)
        log.info(f"Cleaning after test.")
        log.info(f"Closing application.")
        self.app.quit()
