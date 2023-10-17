from locators.Locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Locators import UserAccountPageLocators
import allure

class UserAccountPage:

    def __init__(self, driver):
        self.driver = driver

    def waitForUserAccountContent(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, UserAccountPageLocators.user_account_page_content_xpath)))

    def waitForSeccessMessage(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, UserAccountPageLocators.seccess_message_xpath)))

    # znajduje button "Zmień hasło" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zmień hasło" w panelu klienta')
    def clickAccountData(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, UserAccountPageLocators.account_data_button_xpath))).click()

    # znajduje button "Zmień hasło" oraz klika w niego
    @allure.step('Klikanie w checkbox "Zmień hasło" w panelu klienta')
    def clickResetPassword(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, UserAccountPageLocators.reset_password_checkbox_xpath))).click()

    # znajduje pole do wprowadzenia aktualnego hasła oraz wpisuje dane, które znajdują się pod zmienną 'password'
    @allure.step('Wpisywanie aktualnego hasła')
    def setUserActualPassword(self, password):
        self.driver.find_element_by_id(UserAccountPageLocators.current_password_id).clear()
        self.driver.find_element_by_id(UserAccountPageLocators.current_password_id).send_keys(password)

    # znajduje pole do wprowadzenia nowego hasła oraz wpisuje dane, które znajdują się pod zmienną 'new_password'
    @allure.step('Wpisywanie nowego hasła')
    def setUserNewPassword(self, new_password):
        self.driver.find_element_by_id(UserAccountPageLocators.new_password_id).clear()
        self.driver.find_element_by_id(UserAccountPageLocators.new_password_id).send_keys(new_password)

    # znajduje pole do wprowadzenia potwierdzenia nowego hasła oraz wpisuje dane, które znajdują się pod zmienną 'new_password'
    @allure.step('Potwierdzenie nowego hasła')
    def setConfirmUserNewPassword(self, new_password):
        self.driver.find_element_by_id(UserAccountPageLocators.confirm_new_password_id).clear()
        self.driver.find_element_by_id(UserAccountPageLocators.confirm_new_password_id).send_keys(new_password)

    def waitForSaveButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, UserAccountPageLocators.save_button_xpath)))

    # znajduje button "ZZapisz" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zapisz" w formularzu zmiany hasła')
    def clickSaveButton(self):
        self.waitForSaveButton
        self.driver.find_element_by_xpath(UserAccountPageLocators.save_button_xpath).click()

    @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Moje zamówienia"')
    def AssertHappyPass(self):
        assert "Moje konto" in self.driver.title

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o pomyślnej zmianie hasła')
    def AssertPasswordChanged(self):
        assert "Dane konta zostały zapisane." in self.driver.find_element_by_xpath('//div[@class="message-success success message"]').text