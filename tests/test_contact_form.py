import pytest
from pages.MainPage import MainPage
from pages.ContactFormPage import ContactFormPage
import allure

@pytest.mark.usefixtures('setup')
class Test_ContactForm:

    @allure.title('Weryfikacja działania formularzu kontaktowego')
    def test_contact_form(self):
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.cf = ContactFormPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.clickContactForm()
        self.cf.waitForContactFormPageContent()
        self.cf.SetContactFormUserName(self.env['NAME'])
        self.cf.SetContactFormEmail(self.env['EMAIL'])
        self.cf.SetContactFormPhone(self.env['PHONE'])
        self.cf.SetContactFormComment(self.env['COMMENT'])
        self.cf.clickSendButton()
        self.cf.AssertContactFormSent()

# pytest --env=stage tests\test_contact_form.py