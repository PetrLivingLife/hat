from application import AbstractAppUi, BaseScreen, AppElement


class AppUi(AbstractAppUi):
    """Represents and contains all screens, their elements and possible actions.

    Any screen you want to use in tests, should be instanced under this object.
    e.g.
      self.home_screen = app_screens.home.HomeScreen(self)
    """

    def _setup(self,):
        self.home_screen = HomeScreen(self.platform_driver)


class HomeScreen(BaseScreen):
    SEARCH_FIELD = AppElement(
        browser='input[name="q"]',
        android='//xpath',
        ios='XCUITestElementField.search',
        )  # Google
    # SEARCH_FIELD = AppElement(browser='div.search-form input')  # Seznam

    def search(self, term: str):
        self.SEARCH_FIELD.fill(term)
        self.SEARCH_FIELD.press("Enter")
        self.wait_for_search_results()

    def wait_for_search_results(self,):
        pass
