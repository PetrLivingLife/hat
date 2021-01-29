from .drivers import Chrome, Firefox, Android, Ios
from .app_ui import AppUi

from unittest import TestCase as _TestCase

import logging

from configuration import configuration as cfg


class BaseTest(_TestCase):

    def setUp(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.info(f"Test case setup")
        self.app = AppUi(Firefox())
        # self.app = AppUi(Chrome())
        # self.app.go_to_url(cfg.URL)

    def tearDown(self) -> None:
        self.log.info(f"Closing application.")
        self.app.quit()
