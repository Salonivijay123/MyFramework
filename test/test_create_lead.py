from pages.Create_Lead import CreateLead
from test.test_base import BaseTest
from pages.login_page import LoginPage

class Test_create_leads(BaseTest):
    def test_login(self):
        a=LoginPage(self.driver)
        a.get_homepage(self.config["base_url"])
        a.get_login()
    def test_create_leads(self):
        l = CreateLead(self.driver)
        l.get_homepage(self.config["base_url"])
        l.enter_lead_data()



