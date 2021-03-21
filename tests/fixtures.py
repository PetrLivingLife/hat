import logging
from pytest import fixture

from configuration import setup_logging
from google import GoogleUi
import hat


log = logging.getLogger(__name__)


@fixture(autouse=True, scope='session')
def logging_():
    setup_logging()


@fixture
def platform_driver():
    _platform_driver = hat.start_platform_driver('chromium', headless=False)
    yield _platform_driver
    teardown(_platform_driver)


@fixture
def app(platform_driver):
    platform_driver.open_app(f"https://google.com")
    # platform_driver.open_app(f"https://seznam.cz")
    yield GoogleUi(platform_driver)


def teardown(platform_driver):
    log.info(f"Cleaning after test.")
    log.info(f"Closing application.")
    platform_driver.close()
