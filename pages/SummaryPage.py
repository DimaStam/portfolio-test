from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Locators import SummaryPageLocators
from locators.Locators import PaymentPageLocators
import allure


class SummaryPage:
    page_loader_xpath = '//img[@title="Loading..."] | //img[@alt="Ładuję..."]'

    def __init__(self, driver):
        self.driver = driver

    def waitForPageLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.page_loader_xpath)))

    def waitForCheckoutSummaryPageContent(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, SummaryPageLocators.summary_page_content_xpath)))

    @allure.step('Wybór opcji opłaty PayU')
    def selectPayU(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.payU_xpath).click()

    @allure.step('Wybór opcji opłaty Blik')
    def selectBlik(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.blik_xpath).click()

    @allure.step('Wybór opcji opłaty Apple Pay')
    def selectApplePay(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.apple_pay_xpath).click()

    @allure.step('Wybór opcji opłaty Raty PayU')
    def selectRatyPayU(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.raty_payU_xpath).click()

    @allure.step('Wybór opcji opłaty Raty Credit Agricole')
    def selectRatyCA(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.raty_CA_xpath).click()

    @allure.step('Wybór opcji opłaty Twisto')
    def selectTwisto(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.twisto_xpath).click()

    @allure.step('Wybór opcji opłaty Przelew Tradycyjny')
    def selectBankTransfer(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.bank_transfer_xpath).click()

    @allure.step('Wybór opcji opłaty PayPal')
    def selectPayPal(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.paypal_xpath).click()

    @allure.step('Zaznaczenie pierwszego checkboxa')
    def clickCheckbox1(self):
        self.waitForPageLoaders()
        self.driver.find_element_by_id(SummaryPageLocators.agreement_1_id).click()

    def clickSetCommentButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.XPATH, SummaryPageLocators.set_comment_button_xpath)))

    @allure.step('Wpisywanie komentarza')
    def setComment(self, comment):
        self.driver.find_element_by_xpath(SummaryPageLocators.comment_input_xpath).send_keys(comment)

    @allure.step('Klikanie w przycisk "Zamawiam i płacę"')
    def clickOrderAndPayButton(self):
        self.waitForPageLoaders()
        self.driver.find_element_by_xpath(SummaryPageLocators.order_and_pay_button_xpath).click()

    def waitForPayUPaymentPage(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, PaymentPageLocators.paU_page_content_xpath)))

    @allure.step('Sprawdzenie title strony')
    def AssertPayUTitle(self):
        assert "PayU" in self.driver.title

    @allure.step('Sprawdzenie title strony')
    def AssertRatyCATitle(self):
        assert "Bank Credit Agricole - Crédit Agricole" in self.driver.title

    @allure.step('Sprawdzenie title strony')
    def AssertPayPalTitle(self):
        assert "Zaloguj się do swojego konta PayPal" in self.driver.title

    @allure.step('Sprawdzenie title strony')
    def AssertBlikTitle(self):
        assert "Autoryzacja transakcji" in self.driver.title

    @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Dziękujemy za złożenie zamówienia!"')
    def AssertSuccessPage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dziękujemy za złożenie zamówienia!')]")))
        assert True