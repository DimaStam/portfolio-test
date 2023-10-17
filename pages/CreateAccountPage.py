from locators.Locators import LoginPageLocators
from locators.Locators import CreateAccountPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CreateAccountPage:
    
    def __init__(self, driver):
        self.driver = driver

    def waitForLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.customer_account_icon_xpath)))
    
    @allure.step('Klikanie w ikonkę logowania')
    def clickAccountIcon(self):
        self.waitForLoginButton()
        self.driver.find_element_by_xpath(LoginPageLocators.customer_account_icon_xpath).click()

    def waitForCreateAccountButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, CreateAccountPageLocators.create_account_button_xpath)))
        
    @allure.step('Klikanie w przycisk "Zarejestruj się" na stronie głównej')
    def clickCreateAccountButton(self):
        self.waitForCreateAccountButton()
        self.driver.find_element_by_xpath(CreateAccountPageLocators.create_account_button_xpath).click()

    def waitForCreateAccountForm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, CreateAccountPageLocators.create_account_form_xpath)))

    @allure.step('Wpisywanie danych Name')
    def setName(self, name):
        self.driver.find_element_by_id(CreateAccountPageLocators.name_id).clear()
        self.driver.find_element_by_id(CreateAccountPageLocators.name_id).send_keys(name)

    @allure.step('Wpisywanie danych lastname')
    def setUserLastname(self, lastname):
        self.driver.find_element_by_id(CreateAccountPageLocators.lastname_id).clear()
        self.driver.find_element_by_id(CreateAccountPageLocators.lastname_id).send_keys(lastname)

    @allure.step('Wpisywanie danych username')
    def setEmail(self, email_id):
        self.driver.find_element_by_id(CreateAccountPageLocators.email_id).clear()
        self.driver.find_element_by_id(CreateAccountPageLocators.email_id).send_keys(email_id)

    @allure.step('Wpisywanie danych password')
    def setUserPassword(self, password):
        self.driver.find_element_by_id(CreateAccountPageLocators.password_input_id).clear()
        self.driver.find_element_by_id(CreateAccountPageLocators.password_input_id).send_keys(password)

    @allure.step('Wpisywanie danych confirm password')
    def setUserPasswordConf(self, password):
        self.driver.find_element_by_id(CreateAccountPageLocators.password_conf_input_id).clear()
        self.driver.find_element_by_id(CreateAccountPageLocators.password_conf_input_id).send_keys(password)

    def waitForSighInButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, CreateAccountPageLocators.sign_in_button_xpath)))

    @allure.step('Klikanie w przycisk "Zarejestruj się" w oknie rejestracji')
    def clickSighInButton(self):
        self.waitForSighInButton()
        self.driver.find_element_by_xpath(CreateAccountPageLocators.sign_in_button_xpath).click()

    @allure.step('Klikanie w przycisk "Kup bez rejestracji"')
    def clickContinueAsGuest(self):
        self.driver.find_element_by_xpath(CreateAccountPageLocators.continue_as_guest_button_xpath).click()

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o pomylnym założeniu konta')
    def AssertRegistrationSuccess(self):
        assert 'Dziękujemy za założenie konta!' in self.driver.find_element_by_xpath('//div[@class="message-success success message"]').text

        
