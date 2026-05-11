
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

UN = (By.NAME,'user_name')
PASS = (By.NAME,'user_password')
SUBMIT = (By.ID,'submitButton')
HOME = (By.XPATH,"//a[contains(text(),'Home')]")


class LoginPage(BasePage):
    def get_homepage(self, base_url):
        self.get_url(base_url)

    def get_login(self):
        self.send_keys(UN,"admin")
        self.send_keys(PASS,"admin")
        self.click_element(SUBMIT)
    def verify_login(self):
        element = self.find_element(HOME)
        assert element.is_displayed(),"login test has been failed"

