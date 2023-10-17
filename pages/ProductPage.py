from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Locators import ProductPageLocators
import allure

class ProductPage:
    
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

    @allure.step('Klikanie "OK" w popupie')
    def clickOkInPopup(self):
        self.driver.switch_to.alert.accept()
    