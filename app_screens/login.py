from base.screen import BaseScreen, AppElement, Locator
from selenium.webdriver.common.by import By


class LoginScreen(BaseScreen):
    username_field = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "input.username"),
                                android_locator=Locator(By.CLASS_NAME, "com.input.username"),
                                )
    password_field = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "input.passowrd"),
                                android_locator=Locator(By.CLASS_NAME, "conm.input.password"),
                                )
    login_button = AppElement(browser_locator=Locator(By.CSS_SELECTOR, "button.submit"),
                              android_locator=Locator(By.CLASS_NAME, "com.button.submit")
                              )

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()
        # wait for load
