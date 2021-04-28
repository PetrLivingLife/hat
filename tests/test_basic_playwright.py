import logging

from application import AppElement
import drivers

from test_applications.google import GoogleUi
from tests.base_test import BaseTest


log = logging.getLogger(__name__)


def test_simple_search(app: GoogleUi):
    app.home_screen.search("chata")
    log.info(f"Title: {app.driver.application_instance.title()}")


def test_search_with_app_elements(app):
    app.home_screen.SEARCH_FIELD.type("chata")
    app.home_screen.SEARCH_FIELD.press("Enter")
    log.info(f"Title: {app.driver.application_instance.title()}")


def test_directly_using_locators(app):
    search_field = app.driver.get_element('input[name="q"]')
    search_field.type("chata")
    search_field.press("Enter")
    log.info(f"Title: {app.driver.application_instance.title()}")


def test_app_element_locators_specified_with_dictionary(app):
    search_field_element = AppElement(locator_dictionary={"browser": "input[name='q']"})
    log.info(f"Search field element attributes: {search_field_element.__dict__}")
    search_field = app.driver.get_element(search_field_element.browser)
    search_field.type("chata")
    search_field.press("Enter")
    log.info(f"Title: {app.driver.application_instance.title()}")


def test_use_platform_driver_directly(app, driver):
    search_field = driver.get_element('input[name="q"]')
    search_field.type("chata")
    search_field.press("Enter")
    log.info(f"Title: {app.driver.application_instance.title()}")


def test_new_tab(driver: drivers.Driver):
    from time import sleep
    # TODO And this is the dumm part - this is why I need to find better naming/structure
    # my own custom platform driver.playwright.new_page()
    driver.native_driver.new_page()
    # sleep(5)
    driver.native_driver.new_page()
    driver.native_driver.new_page()
    # sleep(5)


class TestClass(BaseTest):
    # Test also the class approach.

    def test_simple_search(self,):
        self.app.home_screen.search("chata")
        log.info(f"Title: {self.app.driver.application_instance.title()}")

    def test_multiple_tests_in_class(self,):
        self.app.home_screen.search("chata")
        log.info(f"Title: {self.app.driver.application_instance.title()}")
