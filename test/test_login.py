
from test.test_base import BaseTest
from pages.login_page import LoginPage

class LoginPageTest(BaseTest):
    def test_login(self):
        s = LoginPage(self.driver)
        s.get_homepage(self.config["base_url"])
        s.get_login()
        s.verify_login()
