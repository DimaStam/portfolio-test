import pytest
import allure
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage

@pytest.mark.usefixtures('setup')
class TestSearch:

    @allure.title('4.2.1 Wyszukiwarka dla fraz istniejących')
    def test_search_existing_fraze(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchExistingFraze(self.env['EXISTING_PHRASE'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.AssertSearchPositive()

    @allure.title('4.2.2 Wyszukiwarka dla fraz nieistniejących')
    def test_search_not_existing_fraze(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchNotExistingFraze(self.env['NOT_EXISTING_PHRASE'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.AssertSearchNegative()

    @allure.title('4.2.3 Wyszukiwarka dla pojedynczego znaku')
    def test_search_single_character_fraze(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchSingleCharacter(self.env['SINGLE_CHARACTER_PHRASE'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.AssertSearchPositive()

    @allure.title('4.2.3 Wyszukiwarka dla znaku specjalnego')
    def test_search_special_character_fraze(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchSpecialCharacter(self.env['SPECIAL_CHARACTER_PHRASE'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.AssertSearchNegative()

    @allure.title('4.2.4 Wyszukiwarka dla zapytania SQL')
    def test_search_sql_request(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchSQLrequest(self.env['SQL_REQUEST'])
        self.sp.waitForSearchResultPage()
        self.sp.AssertSearchNegative()
