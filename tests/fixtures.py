import logging
from pytest import fixture

from google import GoogleUi
from hat import Hat


log = logging.getLogger(__name__)


@fixture
def hat():
    log.info(f"Starting Hat.")
    return Hat()


@fixture
def platform_driver(hat: Hat):
    log.info(f"Starting platform and driver.")
    return hat.start_platform_driver('chromium', headless=False)


@fixture
def app(platform_driver):
    platform_driver.open_app(f"https://google.com")
    # platform_driver.open_app(f"https://seznam.cz")
    yield GoogleUi(platform_driver)
    teardown(platform_driver)


def teardown(platform_driver):
    log.info(f"Cleaning after test.")
    log.info(f"Closing application.")
    platform_driver.close()
