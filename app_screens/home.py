from base.screen import BaseScreen, AppElement, Locator
from selenium.webdriver.common.by import By


class HomeScreen(BaseScreen):
    home_button = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "button.home"),
                             android_locator=Locator(By.CLASS_NAME, "com.button.home"),
                             )
    login_link = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "a.login"),
                            android_locator=Locator(By.CSS_SELECTOR, "com.link.login"),
                            )
