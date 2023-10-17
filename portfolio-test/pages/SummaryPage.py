from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
import time
from locators.Locators import SummaryPageLocators
from locators.Locators import PaymentPageLocators
import allure


class SummaryPage:
    # payU_xpath = SummaryPageLocators.payU_xpath
    # blik_xpath = SummaryPageLocators.blik_xpath
    # apple_pay_xpath = SummaryPageLocators.apple_pay_xpath
    # raty_payU_xpath = SummaryPageLocators.raty_payU_xpath
    # raty_CA_xpath = SummaryPageLocators.raty_CA_xpath
    # twisto_xpath = SummaryPageLocators.twisto_xpath
    # bank_transfer_xpath = SummaryPageLocators.bank_transfer_xpath
    # paypal_xpath = SummaryPageLocators.paypal_xpath
    # agreement_1_id = SummaryPageLocators.agreement_1_id
    # agreement_2_id = SummaryPageLocators.agreement_2_id
    # order_and_pay_button_xpath = SummaryPageLocators.order_and_pay_button_xpath
    # loader_1 = '//img[@title="Loading..."]'
    # loader_2 = '//img[@alt="Ładuję..."]'
    
    
    # def __init__(self, driver):
    #     self.driver = driver

    # def waiting_for_loaders(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     wait.until(EC.invisibility_of_element((By.XPATH, self.loader_1)))
    #     wait.until(EC.invisibility_of_element((By.XPATH, self.loader_2)))

    # @allure.step('Wybór opcji opłaty PayU')
    # def selectPayU(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     payu_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.payU_xpath)))
    #     if payu_select.is_displayed():
    #         payu_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         payu_select.click()

    # @allure.step('Wybór opcji opłaty Blik')
    # def selectBlik(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     blik_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.blik_xpath)))
    #     if blik_select.is_displayed():
    #         blik_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         blik_select.click()

    # @allure.step('Wybór opcji opłaty Apple Pay')
    # def selectApplePay(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     apple_pay__select = wait.until(EC.element_to_be_clickable((By.XPATH, self.apple_pay_xpath)))
    #     if apple_pay__select.is_displayed():
    #         apple_pay__select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         apple_pay__select.click()

    # @allure.step('Wybór opcji opłaty Raty PayU')
    # def selectRatyPayU(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     raty_payu__select = wait.until(EC.element_to_be_clickable((By.XPATH, self.raty_payU_xpath)))
    #     if raty_payu__select.is_displayed():
    #         raty_payu__select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         raty_payu__select.click()

    # @allure.step('Wybór opcji opłaty Raty Credit Agricole')
    # def selectRatyCA(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     raty_ca_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.raty_CA_xpath)))
    #     if raty_ca_select.is_displayed():
    #         raty_ca_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         raty_ca_select.click()

    # @allure.step('Wybór opcji opłaty Twisto')
    # def selectTwisto(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     twisto_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.twisto_xpath)))
    #     if twisto_select.is_displayed():
    #         twisto_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         twisto_select.click()

    # @allure.step('Wybór opcji opłaty Przelew Tradycyjny')
    # def selectBankTransfer(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     bank_transfer_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.bank_transfer_xpath)))
    #     if bank_transfer_select.is_displayed():
    #         bank_transfer_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         bank_transfer_select.click()

    # @allure.step('Wybór opcji opłaty PayPal')
    # def selectPayPal(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     self.waiting_for_loaders()
    #     paypal_select = wait.until(EC.element_to_be_clickable((By.XPATH, self.paypal_xpath)))
    #     if paypal_select.is_displayed():
    #         paypal_select.click()
    #     else:
    #         self.waiting_for_loaders()
    #         paypal_select.click()

    # @allure.step('Zaznaczenie pierwszego checkboxa')
    # def clickCheckbox1(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     self.waiting_for_loaders()
    #     checkbox_1 = wait.until(EC.element_to_be_clickable((By.ID, self.agreement_1_id)))
    #     if checkbox_1.is_displayed():
    #         checkbox_1.click()
    #     else:
    #         self.waiting_for_loaders()
    #         checkbox_1.click()

    # @allure.step('Zaznaczenie drugiego checkboxa')
    # def clickCheckbox2(self):
    #     wait = WebDriverWait(self.driver, 20)
    #     wait.until(EC.element_to_be_clickable((By.ID, self.agreement_2_id))).click()
    
    # @allure.step('Klikanie w przycisk "Zamawiam i płacę"')
    # def clickOrderAndPayButton(self):
    #     wait = WebDriverWait(self.driver, 15)
    #     self.waiting_for_loaders()
    #     order_and_pay_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.order_and_pay_button_xpath)))
    #     if order_and_pay_button.is_displayed():
    #         order_and_pay_button.click()
    #     else:
    #         self.waiting_for_loaders()
    #         order_and_pay_button.click()

    # @allure.step('Sprawdzenie title strony')
    # def AssertPayUTitle(self):
    #     assert "PayU" in self.driver.title

    # @allure.step('Sprawdzenie title strony')
    # def AssertBlikTitle(self):
    #     assert "Autoryzacja transakcji" in self.driver.title

    # @allure.step('Sprawdzenie title strony')
    # def AssertRatyCATitle(self):
    #     assert "Bank Credit Agricole - Crédit Agricole" in self.driver.title

    # @allure.step('Sprawdzenie title strony')
    # def AssertPayPalTitle(self):
    #     assert "Zaloguj się do swojego konta PayPal" in self.driver.title

    # @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Dziękujemy za złożenie zamówienia!"')
    # def AssertSuccessPage(self):
    #     wait = WebDriverWait(self.driver, 30)
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dziękujemy za złożenie zamówienia!')]")))
    #     assert True

    loader_1 = '//img[@title="Loading..."]'
    loader_2 = '//img[@alt="Ładuję..."]'
    loader_3 = '//div[@class="loading-mask"]'
    page_loader_xpath = '//img[@title="Loading..."] | //img[@alt="Ładuję..."]'

    def __init__(self, driver):
        self.driver = driver

    def waitForPageLoaders(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.page_loader_xpath)))

    def waitForCheckoutSummaryPageContent(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, SummaryPageLocators.summary_page_content_xpath)))

    def waiting_for_loaders(self):
        max_wait_time = 30
        wait = WebDriverWait(self.driver, max_wait_time)
        for _ in range(max_wait_time):
            try: 
                wait.until(EC.invisibility_of_element((By.XPATH, self.loader_1)))
                wait.until(EC.invisibility_of_element((By.XPATH, self.loader_2)))
                wait.until(EC.invisibility_of_element((By.XPATH, self.loader_3)))
            except:
                time.sleep(1)
            else: 
                break

    def click_element_with_loader_check(self, element):
        wait = WebDriverWait(self.driver, 30)
        element_to_click = wait.until(EC.visibility_of_element_located(element))
        try:
            if not element_to_click.is_enabled():
                self.waiting_for_loaders()
            self.driver.execute_script("arguments[0].click();", element_to_click)
        except Exception as e:
            print(f"Exception occurred during click_element_with_loader_check execution: {e}")
            self.waiting_for_loaders()
            self.driver.execute_script("arguments[0].click();", element_to_click)

    @allure.step('Wybór opcji opłaty PayU')
    def selectPayU(self):
        self.driver.find_element_by_xpath(SummaryPageLocators.payU_xpath).click()

    @allure.step('Wybór opcji opłaty Blik')
    def selectBlik(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.blik_xpath))

    @allure.step('Wybór opcji opłaty Apple Pay')
    def selectApplePay(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.apple_pay_xpath))

    @allure.step('Wybór opcji opłaty Raty PayU')
    def selectRatyPayU(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.raty_payU_xpath))

    @allure.step('Wybór opcji opłaty Raty Credit Agricole')
    def selectRatyCA(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.raty_CA_xpath))

    @allure.step('Wybór opcji opłaty Twisto')
    def selectTwisto(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.twisto_xpath))

    @allure.step('Wybór opcji opłaty Przelew Tradycyjny')
    def selectBankTransfer(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.bank_transfer_xpath))

    @allure.step('Wybór opcji opłaty PayPal')
    def selectPayPal(self):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.paypal_xpath))

    @allure.step('Zaznaczenie pierwszego checkboxa')
    def clickCheckbox1(self):
        self.waitForPageLoaders()
        self.driver.find_element_by_id(SummaryPageLocators.agreement_1_id).click()

    @allure.step('Wpisywanie komentarza')
    def setComment(self, comment):
        self.click_element_with_loader_check((By.XPATH, SummaryPageLocators.comment_button_xpath))
        self.driver.find_element_by_xpath(SummaryPageLocators.comment_field_xpath).send_keys(comment)

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