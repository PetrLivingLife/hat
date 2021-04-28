import logging

from pytest import fixture

from configuration import setup_logging

import application
import drivers
import hat

from test_applications.google import GoogleUi


log = logging.getLogger(__name__)


@fixture(autouse=True, scope='session')
def logging_():
    setup_logging()


@fixture
def driver() -> drivers.Driver:
    driver_ = hat.start_driver('chromium', headless=False, locale='en-GB')
    yield driver_
    teardown(driver_)


@fixture
def app(driver) -> application.Application:
    driver.open_app(f"https://google.com")
    # driver.open_app(f"https://seznam.cz")
    yield GoogleUi(driver)


def teardown(driver):
    log.info(f"Cleaning after test.")
    log.info(f"Closing application.")
    driver.quit()
