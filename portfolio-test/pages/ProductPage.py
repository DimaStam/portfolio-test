from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Locators import ProductPageLocators
from locators.Locators import LoginPageLocators
import allure

class ProductPage:
    add_to_cart_button_id = ProductPageLocators.add_to_cart_button_id
    input_xpath = ProductPageLocators.input_xpath
    delete_from_cart_xpath = ProductPageLocators.delete_from_cart_xpath
    
    def __init__(self, driver):
        self.driver = driver

    def waitForProductPage(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, ProductPageLocators.product_page_content_xpath)))

    def waitForAddToCartButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.ID, ProductPageLocators.add_to_cart_button_id)))

    @allure.step('Klikanie w przycisk "Dodaj do koszyka"')
    def clickAddToCartButton(self):
        self.waitForAddToCartButton()
        self.driver.find_element_by_id(ProductPageLocators.add_to_cart_button_id).click()

    # @allure.step('Wpisywanie wartości na KP produktu')
    # def setInputValue(self, value_1):
    #     wait = WebDriverWait(self.driver, 15)
    #     set_input_value = wait.until(EC.presence_of_element_located((By.XPATH, self.input_xpath)))
    #     set_input_value.send_keys(Keys.CONTROL + "a")
    #     set_input_value.send_keys(Keys.DELETE)
    #     set_input_value.send_keys(value_1)
    #     set_input_value.send_keys(Keys.TAB)

    # @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat niedostępności produktu')
    # def AssertProductNotAvailable(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="modal-content"]/div/section[1]')))
    #     assert "Nie posiadamy tylu sztuk" in self.driver.find_element_by_xpath('//div[@class="modal-content"]/div/section[1]').text

    @allure.step('Klikanie "OK" w popupie')
    def clickOkInPopup(self):
        self.driver.switch_to.alert.accept()
    