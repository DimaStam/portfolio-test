from locators.Locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

class MainPage:

    menu_kategorie_xpath = MainPageLocators.menu_kategorie_xpath
    kategorie_href_xpath = MainPageLocators.kategorie_href_xpath
    podkategorie_href_xpath = MainPageLocators.podkategorie_href_xpath
    search_input_id = MainPageLocators.search_input_id
    search_button_xpath = MainPageLocators.search_button_xpath
    accept_cookies_xpath = MainPageLocators.accept_cookies_xpath
    contact_form_button_xpath = MainPageLocators.contact_form_button_xpath


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie istniejącej frazy')
    def SearchExistingFraze(self, existing_fraze):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id))).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(existing_fraze)

    def waitForMainPage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, MainPageLocators.main_page_content_id)))

    def waitForSearchButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath)))

    @allure.step('Klikanie w przycisk "Wyszukaj"')
    def clickSearchButton(self):
        self.waitForSearchButton()
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie nieistniejącej frazy')
    def SearchNotExistingFraze(self, not_existing_fraze):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id))).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(not_existing_fraze)

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie znaku pojedynczego')
    def SearchSingleCharacter(self, single_character_fraze):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id))).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(single_character_fraze)

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie znaku specjalnego')
    def SearchSpecialCharacter(self, special_character_fraze):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id))).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(special_character_fraze)

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie zapytania SQL')
    def SearchSQLrequest(self, SQL_request):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id))).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(SQL_request, Keys.RETURN)

    def waitForContactFormButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, MainPageLocators.contact_form_button_xpath)))

    @allure.step('Wyszukiwanie przyciska "Formularz kontaktowy" oraz klikanie w niego')
    def clickContactForm(self):
        action = ActionChains(self.driver)
        contact_form_button = self.driver.find_element_by_xpath(MainPageLocators.contact_form_button_xpath)
        self.waitForContactFormButton()
        action.move_to_element(contact_form_button).perform()
        contact_form_button.click()

    def waitForCookieBar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.accept_cookies_xpath)))

    @allure.step('Wyszukiwanie przyciska "Akceptuję" pliki cookie oraz klikanie w niego')
    def clickAcceptCookies(self):
        self.waitForCookieBar()
        self.driver.find_element_by_xpath(MainPageLocators.accept_cookies_xpath)

    def waitForSearchBar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.search_input_id)))

    @allure.step('Znajdowanie pola wyszukiwarki oraz wpisywanie słowa Żarówka')
    def SearchProduct(self, search_keyword):
        self.waitForSearchBar()
        self.driver.find_element_by_id(self.search_input_id).send_keys(search_keyword)