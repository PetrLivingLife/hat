from application import Application, AppElement, Screen


class GoogleUi(Application):

    def _setup(self,):
        self.home_screen = HomeScreen(self.driver)


class HomeScreen(Screen):
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
