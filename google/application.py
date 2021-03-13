from application import AbstractAppUi, AppElement, BaseScreen


class GoogleUi(AbstractAppUi):
    """Represents and contains all screens, their elements and possible actions.

    Any screen you want to use in tests, should be instanced within _setup method.
    It gets automatically called when AppUi is initialized before test.
    e.g.
      self.home_screen = HomeScreen(self.platform_driver)
    """

    def _setup(self,):
        self.home_screen = HomeScreen(self.platform_driver)


class HomeScreen(BaseScreen):
    SEARCH_FIELD = AppElement(
        browser='input[name="q"]',
        android='//xpath',
        ios='XCUITestElementField.search',
        )

    def search(self, term: str):
        self.SEARCH_FIELD.fill(term)
        self.SEARCH_FIELD.press("Enter")
        self.wait_for_search_results()

    def wait_for_search_results(self,):
        pass
