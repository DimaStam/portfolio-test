import pytest
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ExtraoptionsPage import ExtraoptionsPage
import allure

@pytest.mark.usefixtures('setup')
class Test_Extraoptions:

    @allure.title('Test grawerowania na produkcie')
    def test_engraver_product(self):
        # pytest.skip()
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.driver.get(self.env['URL'])
        self.mp.waitForMainPage()
        self.mp.SearchProduct(self.env['SEARCH_KEYWORD'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.selectFirstItem()
        self.pp.waitForProductPage()
        self.pp.clickAddToCartButton()
        self.ex.waitForExtraoptionsPageContent()
        self.ex.clickEngraveProductCheckbox()
        self.ex.waitForEngravePopup()
        self.ex.clickEngraveOrderButton()
        self.ex.AssertEngraverStyleErrorExist()
        self.ex.clickEngraveA()
        self.ex.clickEngraveB()
        self.ex.clickEngraveC()
        self.ex.clickEngraveOrderButton()
        self.ex.AssertEngraverStyleErrorNotExist()
        self.ex.AssertEngraverMessageErrorExist()
        self.ex.setEngraverMessage()
        self.ex.clickEngraveOrderButton()

# pytest --env=stage tests\test_extraoptions.py
