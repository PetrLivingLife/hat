import logging

from test_applications.google import GoogleUi
import hat


class BaseTest(object):
    # Class approach can't mix with fixtures (function approach). So the setup code and teardown is duplicated here.

    def setup_method(self):
        self.log = logging.getLogger(__name__)
        self.log.info(f"Test case setup")

        try:
            self.driver = hat.start_driver('chromium')
            self.driver.open_app(f"https://google.com")
            self.app = GoogleUi(self.driver)
        except Exception as e:
            try:
                self.teardown_method()
            except Exception as _e:
                raise _e
            raise e

    def teardown_method(self):
        self.log.info(f"Cleaning after test.")
        self.log.info(f"Closing application.")
        self.driver.close()
