from locators.Locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def waitForLoginPage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.login_page_content_xpath)))

    @allure.step('Klikanie w ikonkę logowania')
    def clickAccountIcon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, LoginPageLocators.customer_account_icon_xpath))).click()

    @allure.step('Wpisywanie danych username')
    def setUserName(self, username):
        self.driver.find_element_by_id(LoginPageLocators.email_input_id).clear()
        self.driver.find_element_by_id(LoginPageLocators.email_input_id).send_keys(username)

    @allure.step('Wpisywanie danych password')
    def setUserPassword(self, password):
        self.driver.find_element_by_id(LoginPageLocators.password_input_id).clear()
        self.driver.find_element_by_id(LoginPageLocators.password_input_id).send_keys(password)

    @allure.step('Klikanie w przycisk "Zaloguj się"')
    def clickLoginButton(self):
        self.driver.find_element_by_xpath(LoginPageLocators.login_button_xpath).click()

    def waitForAlertMessage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.alert_message_xpath)))

    @allure.step('Klikanie w przycisk "Wyloguj się"')
    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.logout_button_xpath))).click()

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o wpisaniu nieprawidowych danych')
    def AssertUnhappyPass(self):
        assert "Logowanie się nie udało :( Sprawdź poprawność danych i spróbuj ponownie" in self.driver.find_element_by_xpath(LoginPageLocators.alert_message_xpath).text
    