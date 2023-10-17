from locators.Locators import CheckoutDeliveryLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class CheckoutDeliveryPage:
    loader_1 = '//img[@title="Loading..."]'
    loader_2 = '//img[@alt="Ładuję..."]'

    page_loader_xpath = '//img[@title="Loading..."] | //img[@alt="Ładuję..."]'

    def __init__(self, driver):
        self.driver = driver

    def waitForPageLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.page_loader_xpath)))

    def waitForCheckutAdressForm(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.checkout_adress_form_xpath)))    

    def _wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Wpisywanie danych w polu "E-mail"')
    def setEmail(self, email):
        # email_input = self._wait_for_element((By.ID, CheckoutDeliveryLocators.email_input_id))
        email_input = self.driver.find_element_by_id(CheckoutDeliveryLocators.email_input_id)
        email_input.clear()
        email_input.send_keys(email)

    @allure.step('Wpisywanie danych w polu "Telefon"')
    def setPhoneNumber(self, phone):
        phone_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.phone_input_xpath))
        phone_input.clear()
        phone_input.send_keys(phone)

    @allure.step('Wpisywanie danych w polu "Imie"')
    def setFirstName(self, name):
        firstname_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.firstname_input_xpath))
        firstname_input.clear()
        firstname_input.send_keys(name)

    @allure.step('Wpisywanie danych w polu "Nazwisko"')
    def setLastName(self, lastname):
        lastname_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.lastname_input_xpath))
        lastname_input.clear()
        lastname_input.send_keys(lastname)

    @allure.step('Wpisywanie danych w polu "Ulica"')
    def setStreet(self, street):
        street_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.street_input_xpath))
        street_input.clear()
        street_input.send_keys(street)

    @allure.step('Wpisywanie danych w polu "Kod pocztowy"')
    def setPostcode(self, postcode):
        postcode_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.postcode_input_xpath))
        postcode_input.clear()
        postcode_input.send_keys(postcode)
        # self.waitForPageLoaders()

    @allure.step('Wpisywanie danych w polu "Miasto"')
    def setCity(self, city):
        city_input = self._wait_for_element((By.XPATH, CheckoutDeliveryLocators.city_input_xpath))
        city_input.clear()
        city_input.send_keys(city)
        # self.waitForPageLoaders()

    def waitForDeliмeryMethodsBlock(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.delivery_methods_xpath)))

    @allure.step('Zaznaczenie "Kurier DHL"')
    def clickCourierDHL(self):
        wait = WebDriverWait(self.driver, 15)
        click_courier_dhl = wait.until(EC.element_to_be_clickable((By.XPATH, CheckoutDeliveryLocators.courier_dhl_xpath)))
        click_courier_dhl.click()
        self.waitForPageLoaders()

    @allure.step('Zaznaczenie "Inpost Paczkomaty 24/7"')
    def clickInpost(self):
        wait = WebDriverWait(self.driver, 15)
        self.waiting_for_loaders()
        click_inpost = wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.inpost_xpath)))
        if not click_inpost.is_displayed():
            self.waiting_for_loaders()
        click_inpost.click()

    @allure.step('Znajdowanie pola wyszukiwarki Inpost oraz znajdowanie paczkomata WRO06N')
    def SearchInpostAdress(self, paczkomat_adres):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, CheckoutDeliveryLocators.inpost_input_id))).clear()
        self.driver.find_element_by_id(CheckoutDeliveryLocators.inpost_input_id).send_keys(paczkomat_adres, Keys.RETURN)

    @allure.step('Wybór paczkomata z listy')
    def SelectPoint(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.inpost_point_xpath))).click()

    @allure.step('Klickanie w przycisk "Wybierz"')
    def ClickChooseButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.inpost_select_button_xpath))).click()

    @allure.step('Zaznaczenie "UPS Standard"')
    def clickUpsStandard(self):
        wait = WebDriverWait(self.driver, 15)
        self.waiting_for_loaders()
        click_ups_standard = wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.ups_standard_xpath)))
        if not click_ups_standard.is_displayed():
            self.waiting_for_loaders()
        click_ups_standard.click()

    @allure.step('Zaznaczenie "Odbiór w sklepie"')
    def clickFreeShipping(self):
        wait = WebDriverWait(self.driver, 15)
        self.waiting_for_loaders()
        free_shipping_button = wait.until(EC.visibility_of_element_located((By.XPATH, CheckoutDeliveryLocators.freeshipping_xpath)))
        if not free_shipping_button.is_displayed():
            self.waiting_for_loaders()
        free_shipping_button.click()

    def waitForProceedToSummaryButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, CheckoutDeliveryLocators.proceed_to_summary_button_id)))

    @allure.step('Wyszukiwanie przyciska "Zobacz podsumowanie" oraz klikanie w niego')
    def goToCheckoutSummary(self):
        self.waitForProceedToSummaryButton()
        self.driver.find_element_by_id(CheckoutDeliveryLocators.proceed_to_summary_button_id).click()
        self.waitForPageLoaders()

    @allure.step('Sprawdzenie title strony Dostawa')
    def AssertCheckoutDeliveryTitle(self):
        assert "Zamówienie" in self.driver.title

    