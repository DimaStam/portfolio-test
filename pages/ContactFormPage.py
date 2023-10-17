from locators.Locators import ContactPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ContactFormPage:

    def __init__(self, driver):
        self.driver = driver

    def waitForContactFormPageContent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ContactPageLocators.contact_form_page_content_xpath)))
    
    @allure.step('Znajdowanie pola Imię formularzu kontaktowego oraz wpisywanie imienia')
    def SetContactFormUserName(self, name):
        set_user_name = self.driver.find_element_by_id(ContactPageLocators.contact_form_name_id)
        set_user_name.clear()
        set_user_name.send_keys(name)

    @allure.step('Znajdowanie pola Email formularzu kontaktowego oraz wpisywanie emaila')
    def SetContactFormEmail(self, email):
        set_email = self.driver.find_element_by_id(ContactPageLocators.contact_form_email_id)
        set_email.clear()
        set_email.send_keys(email)

    @allure.step('Znajdowanie pola Telefon formularzu kontaktowego oraz wpisywanie numeru')
    def SetContactFormPhone(self, phone):
        set_phone_numer = self.driver.find_element_by_id(ContactPageLocators.contact_form_phone_id)
        set_phone_numer.clear()
        set_phone_numer.send_keys(phone)

    @allure.step('Znajdowanie pola Zostaw nam wiadomość formularzu kontaktowego oraz wpisywanie wiadomości')
    def SetContactFormComment(self, comment):
        set_comment = self.driver.find_element_by_id(ContactPageLocators.contact_form_comment_id)
        set_comment.clear()
        set_comment.send_keys(comment)

    @allure.step('Wyszukiwanie przyciska "Wyślij" oraz klikanie w niego')
    def clickSendButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.send_button_xpath))).click()

    @allure.step('Sprawdzenie czy po wysłaniu formularza mamy odpowiedź "Dziękujemy za skontaktowanie się z nami. Odpowiemy najszybciej jak to będzie możliwe."')
    def AssertContactFormSent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dziękujemy za skontaktowanie się z nami. Odpowiemy najszybciej jak to będzie możliwe.')]")))
        assert True