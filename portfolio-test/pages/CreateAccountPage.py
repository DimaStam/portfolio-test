from locators.Locators import LoginPageLocators
from locators.Locators import CreateAccountPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CreateAccountPage:
    customer_account_icon_xpath = LoginPageLocators.customer_account_icon_xpath
    create_account_button_xpath = CreateAccountPageLocators.create_account_button_xpath
    continue_as_guest_button_xpath = CreateAccountPageLocators.continue_as_guest_button_xpath
    name_id = CreateAccountPageLocators.name_id
    lastname_id = CreateAccountPageLocators.lastname_id
    email_id = CreateAccountPageLocators.email_id
    password_input_id = CreateAccountPageLocators.password_input_id
    password_conf_input_id = CreateAccountPageLocators.password_conf_input_id
    sign_in_button_xpath = CreateAccountPageLocators.sign_in_button_xpath
    
    def __init__(self, driver):
        self.driver = driver

    def waitForLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.customer_account_icon_xpath)))
    
    # znajduje przycisk "Zaloguj się" oraz klika w niego
    @allure.step('Klikanie w ikonkę logowania')
    def clickAccountIcon(self):
        self.waitForLoginButton()
        self.driver.find_element_by_xpath(self.customer_account_icon_xpath).click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located((By.XPATH, self.customer_account_icon_xpath))).click()
        
    # znajduje button "Zarejestruj się" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zarejestruj się" na stronie głównej')
    def clickCreateAccountButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.create_account_button_xpath))).click()

    def waitForCreateAccountForm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, CreateAccountPageLocators.create_account_form_xpath)))

    # znajduje pole do wprowadzenia imienia oraz wpisuje dane, które znajdują się pod zmienną 'name'
    @allure.step('Wpisywanie danych Name')
    def setName(self, name):
        self.driver.find_element_by_id(self.name_id).clear()
        self.driver.find_element_by_id(self.name_id).send_keys(name)

    # znajduje pole do wprowadzenia nazwiska oraz wpisuje dane, które znajdują się pod zmienną 'lastname'
    @allure.step('Wpisywanie danych lastname')
    def setUserLastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_id).clear()
        self.driver.find_element_by_id(self.lastname_id).send_keys(lastname)

    # znajduje pole do wprowadzenia emaila oraz wpisuje dane, które znajdują się pod zmienną 'username'
    @allure.step('Wpisywanie danych username')
    def setEmail(self, email_id):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email_id)
    
    # znajduje pole do wprowadzenia hasła oraz wpisuje dane, które znajdują się pod zmienną 'password'
    @allure.step('Wpisywanie danych password')
    def setUserPassword(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    # znajduje pole do wprowadzenia potwierdzenia hasła oraz wpisuje dane, które znajdują się pod zmienną 'password'
    @allure.step('Wpisywanie danych confirm password')
    def setUserPasswordConf(self, password):
        self.driver.find_element_by_id(self.password_conf_input_id).clear()
        self.driver.find_element_by_id(self.password_conf_input_id).send_keys(password)

    def waitForSighInButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, CreateAccountPageLocators.sign_in_button_xpath)))

    # znajduje przycisk "Zarejestruj się" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zarejestruj się" w oknie rejestracji')
    def clickSighInButton(self):
        self.waitForSighInButton()
        self.driver.find_element_by_xpath(CreateAccountPageLocators.sign_in_button_xpath).click()

    # znajduje przycisk "Kup bez rejestracji" oraz klika w niego
    @allure.step('Klikanie w przycisk "Kup bez rejestracji"')
    def clickContinueAsGuest(self):
        self.driver.find_element_by_xpath(self.continue_as_guest_button_xpath).click()

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o pomylnym założeniu konta')
    def AssertRegistrationSuccess(self):
        assert 'Dziękujemy za założenie konta!' in self.driver.find_element_by_xpath('//div[@class="message-success success message"]').text

        
