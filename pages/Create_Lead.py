from selenium.webdriver.common.by import By

from pages.base_page import BasePage


leads = (By.XPATH,"//a[contains(text(),'Leads')]")
Create_leads =(By.XPATH,"//img[@title='Create Lead...']")
dropdown = (By.XPATH,"//select[@name='salutationtype']")
firstname = (By.XPATH,"//input[@name='firstname']")
lastname = (By.XPATH,"//input[@name='lastname']")
company = (By.XPATH,"//input[@name='company']")
title = (By.XPATH,"//input[@name='designation']")
Lead_source = (By.XPATH,"//select[@name='leadsource']")
industry = (By.XPATH,"//select[@name='industry']")
annual_revenue = (By.XPATH,"//input[@name='annualrevenue']")
No_of_Employees = (By.XPATH,"//input[@name='noofemployees']")
secondary_email = (By.XPATH,"//input[@name='secondaryemail']")
phone = (By.XPATH,"//input[@name='phone']")
mobile = (By.XPATH,"//input[@name='mobile']")
fax = (By.XPATH,"//input[@name='fax']")
email = (By.XPATH,"//input[@name='email']")

website = (By.XPATH,"//input[@name='website']")
Lead_status = (By.XPATH,"//select[@name='leadstatus']")
rate = (By.XPATH,"//select[@name='rating']")

assigned = (By.XPATH,"//select[@name='assigned_user_id']")
assigned_radio=(By.CSS_SELECTOR,"input[value='U']")
po_box = (By.XPATH,"//input[@name='pobox']")
city = (By.XPATH,"//input[@name='city']")
state = (By.XPATH,"//input[@name='state']")
postal_code = (By.XPATH,"//input[@name='code']")
country = (By.XPATH,"//input[@name='country']")
street =(By.XPATH,"//textarea[@name='lane']")
description = (By.XPATH,"//textarea[@class='detailedViewTextBox' and @name='description']")
save_button = (By.XPATH,"//input[@class='crmButton small save']")
verify = (By.XPATH,"//span[text() = 'Updated today (13 May 2026) By Admin123@ Administrator1']")

class CreateLead(BasePage):
    def get_homepage(self, base_url):
        self.get_url(base_url)

    def enter_lead_data(self):

        self.click_element(leads)
        self.click_element(Create_leads)
        self.select_from_dropdown(dropdown,"Ms.","text")
        self.send_keys(firstname,"saloni")
        self.send_keys(lastname,"vijayvergiya")
        self.send_keys(company,"exotic india")
        self.send_keys(title,"exotic india pvt ltd")
        self.select_from_dropdown(Lead_source,"Self Generated","value")
        self.select_from_dropdown(industry,"Technology","value")
        self.send_keys(annual_revenue,"100000")
        self.send_keys(No_of_Employees,"222")
        self.send_keys(secondary_email,"saloni@gmail.com")
        self.send_keys(phone,"123456")
        self.send_keys(mobile,"123456")
        self.send_keys(fax,"123456")
        self.send_keys(email,"abs1@gmail.com")
        self.send_keys(website,"website")
        self.select_from_dropdown(Lead_status,"Attempted to Contact","text")
        self.select_from_dropdown(rate,"Acquired","value")
        self.select_radio_button(assigned_radio)
        self.select_from_dropdown(assigned,"34","value")
        self.send_keys(po_box,"110011234")
        self.send_keys(city,"delhi")
        self.send_keys(state,"delhi")
        self.send_keys(postal_code,"123456")
        self.send_keys(country,"india")
        self.send_keys(street,"maharani road")
        self.send_keys(description,"description not required")
        self.click_element(save_button)
        self.handle_alert("accept")
    def verify_lead_data(self):
        element = self.find_element(verify)

        assert "Updated today (13 May 2026) By Admin123@ Administrator1" in element.text()
