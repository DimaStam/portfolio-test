from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.Locators import ShoppingCartPageLocators
import allure

class ShoppingCartPage:
    page_loader_xpath = '//img[@title="Loading..."] | //img[@alt="Ładuję..."]'
    summary_block_loader_xpath = '//img[@title="Loading..."]'
    
    def __init__(self, driver):
        self.driver = driver

    def waitiForSummaryBlockLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element((By.XPATH, self.summary_block_loader_xpath)))

    def waitForPageLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element((By.XPATH, self.page_loader_xpath)))

    def waitForCartPageContent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ShoppingCartPageLocators.cart_page_content_xpath)))

    def waitForProductCountInput(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ShoppingCartPageLocators.product_input_count_xpath)))

    @allure.step('Wpisywanie wartości na KP produktu')
    def setInputValue(self, value_1):
        self.waitForProductCountInput()
        set_input_value = self.driver.find_element_by_xpath(ShoppingCartPageLocators.product_input_count_xpath)
        set_input_value.send_keys(Keys.CONTROL + "a")
        set_input_value.send_keys(Keys.DELETE)
        set_input_value.send_keys(value_1)
        set_input_value.send_keys(Keys.TAB)

    def waitForGoToOrderButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ShoppingCartPageLocators.go_to_order_button_xpath)))

    @allure.step('Kliknięcie przyciska "Dalej"')
    def goToCheckoutDelivery(self):
        self.waitForGoToOrderButton()
        self.driver.find_element_by_xpath(ShoppingCartPageLocators.go_to_order_button_xpath).click()
        self.waitForPageLoaders()

    @allure.step('Sprawdzenie title strony Koszyk')
    def AssertShoppingCartTitle(self):
        assert "Koszyk" in self.driver.title

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat niedostępności produktu')
    def AssertProductNotAvailable(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="modal-content"]/div/section[1]')))
        assert "Nie posiadamy tylu sztuk" in self.driver.find_element_by_xpath('//div[@class="modal-content"]/div/section[1]').text
    