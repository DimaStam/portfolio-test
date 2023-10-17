from locators.Locators import ContactPageLocators
from locators.Locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ContactFormPage:
    accept_cookies_xpath = MainPageLocators.accept_cookies_xpath
    contact_form_name_id = ContactPageLocators.contact_form_name_id
    contact_form_email_id = ContactPageLocators.contact_form_email_id
    contact_form_phone_id = ContactPageLocators.contact_form_phone_id
    contact_form_comment_id = ContactPageLocators.contact_form_comment_id
    send_button_xpath = ContactPageLocators.send_button_xpath

    def __init__(self, driver):
        self.driver = driver


    def waitForContactFormPageContent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ContactPageLocators.contact_form_page_content_xpath)))
    
    @allure.step('Znajdowanie pola Imię formularzu kontaktowego oraz wpisywanie imienia')
    def SetContactFormUserName(self, name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.contact_form_name_id))).clear()
        self.driver.find_element_by_id(self.contact_form_name_id).send_keys(name)

    @allure.step('Znajdowanie pola Email formularzu kontaktowego oraz wpisywanie emaila')
    def SetContactFormEmail(self, email):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.contact_form_email_id))).clear()
        self.driver.find_element_by_id(self.contact_form_email_id).send_keys(email)

    @allure.step('Znajdowanie pola Telefon formularzu kontaktowego oraz wpisywanie numeru')
    def SetContactFormPhone(self, phone):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.contact_form_phone_id))).clear()
        self.driver.find_element_by_id(self.contact_form_phone_id).send_keys(phone)

    @allure.step('Znajdowanie pola Zostaw nam wiadomość formularzu kontaktowego oraz wpisywanie wiadomości')
    def SetContactFormComment(self, comment):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.contact_form_comment_id))).clear()
        self.driver.find_element_by_id(self.contact_form_comment_id).send_keys(comment)

    @allure.step('Wyszukiwanie przyciska "Wyślij" oraz klikanie w niego')
    def clickSendButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.send_button_xpath))).click()

    @allure.step('Sprawdzenie czy po wysłaniu formularza mamy odpowiedź "Dziękujemy za skontaktowanie się z nami. Odpowiemy najszybciej jak to będzie możliwe."')
    def AssertContactFormSent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dziękujemy za skontaktowanie się z nami. Odpowiemy najszybciej jak to będzie możliwe.')]")))
        assert True