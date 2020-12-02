from base.basetest import BaseTest


class Login(BaseTest):

    def test_valid_login(self):
        self.app.login_screen.login("petr", "heslo")
        pass
