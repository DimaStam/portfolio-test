from locators.Locators import ExtraoptionsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class ExtraoptionsPage:
    page_loader_xpath = '//img[@alt="Ładuję..."] | //img[@title="Loading..."]'

    def __init__(self, driver):
        self.driver = driver

    def waitForPageLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.page_loader_xpath)))

    def waitForExtraoptionsPageContent(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ExtraoptionsPageLocators.extraoptions_page_content_xpath)))

    def waitForGoToCartButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, ExtraoptionsPageLocators.go_to_cart_button_xpath)))

    @allure.step('Zaznaczenie checkboxa "Grawerowanie na produkcie"')
    def clickEngraveProductCheckbox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, ExtraoptionsPageLocators.engrave_product_checkbox_xpath))).click()

    def waitForEngravePopup(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ExtraoptionsPageLocators.engrave_popup_area_xpath)))

    @allure.step('Zaznaczenie Wersja A')
    def clickEngraveA(self):
        self.driver.find_element_by_xpath(ExtraoptionsPageLocators.engraver_product_a_xpath).click()

    @allure.step('Zaznaczenie Wersja B')
    def clickEngraveB(self):
        self.driver.find_element_by_xpath(ExtraoptionsPageLocators.engraver_product_a_xpath).click()

    @allure.step('Zaznaczenie Wersja C')
    def clickEngraveC(self):
        self.driver.find_element_by_xpath(ExtraoptionsPageLocators.engraver_product_a_xpath).click()

    def waitForOrderEngraveButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, ExtraoptionsPageLocators.order_engraver_button_xpath)))

    @allure.step('Klikanie w przycisk "Zamawiam grawerowanie"')
    def clickEngraveOrderButton(self):
        self.waitForOrderEngraveButton()
        self.driver.find_element_by_xpath(ExtraoptionsPageLocators.order_engraver_button_xpath).click()

    def waitForEngraveInput(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, ExtraoptionsPageLocators.engraver_product_input_id)))

    @allure.step('Wpisywanie treści grawerunku produktu')
    def setEngraverMessage(self):
        self.waitForEngraveInput()
        set_input_value = self.driver.find_element_by_id(ExtraoptionsPageLocators.engraver_product_input_id)
        set_input_value.send_keys(Keys.CONTROL + "a")
        set_input_value.send_keys(Keys.DELETE)
        set_input_value.send_keys("Treść testowa grawerunku")

    @allure.step('Wyszukiwanie przyciska "Zobacz koszyk" oraz klikanie w niego')
    def goToCheckoutCart(self):
        self.waitForGoToCartButton()
        self.driver.find_element_by_xpath(ExtraoptionsPageLocators.go_to_cart_button_xpath).click()
        self.waitForPageLoaders()

    @allure.step('Sprawdzenie weryfikacji wybotu stylu grawerunku produktu')
    def AssertEngraverStyleErrorExist(self):
        assert 'Wybór stylu jest wymagany' in self.driver.find_element_by_xpath('//div[@class="error"]').text

    @allure.step('Sprawdzenie czy wyświetla się error po zaznaczeniu stylu grawerunku produktu. Odbywa się poprzez sprawdzenie czy kontener z komunikatem jest na stronie')
    def AssertEngraverStyleErrorNotExist(self):
        assert not len(self.driver.find_elements_by_xpath('//div[@class="error"]'))

    @allure.step('Sprawdzenie weryfikacji wpisywanie treści grawerunku produktu')
    def AssertEngraverMessageErrorExist(self):
        assert 'To pole jest wymagane' in self.driver.find_element_by_xpath('//div[@class="mage-error"]').text

    @allure.step('Sprawdzenie title strony Extraoptions')
    def AssertExtraoptionsTitle(self):
        assert "Dodano do koszyka" in self.driver.title