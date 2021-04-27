import logging
from pytest import fixture

from configuration import setup_logging
from test_applications.google import GoogleUi
import hat


log = logging.getLogger(__name__)


@fixture(autouse=True, scope='session')
def logging_():
    setup_logging()


@fixture
def driver():
    driver_ = hat.start_driver('chromium', headless=False, locale='en-GB')
    yield driver_
    teardown(driver_)


@fixture
def app(driver):
    driver.open_app(f"https://google.com")
    # driver.open_app(f"https://seznam.cz")
    yield GoogleUi(driver)


def teardown(driver):
    log.info(f"Cleaning after test.")
    log.info(f"Closing application.")
    driver.quit()
