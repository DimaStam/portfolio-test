import pytest
import allure
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.LoginPage import LoginPage
from pages.ExtraoptionsPage import ExtraoptionsPage

@pytest.mark.usefixtures('setup')
class TestAddToCart:
    value = 150000

    @allure.title('Test dodawania do koszyka')
    def test_add_to_cart(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchProduct(self.env['SEARCH_KEYWORD'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.selectFirstItem()
        self.pp.waitForProductPage()
        self.pp.clickAddToCartButton()
        self.ex.waitForExtraoptionsPageContent()
        self.ex.AssertExtraoptionsTitle()

    @allure.title('Test komunikatu o niedostępności produktu')
    def test_product_not_available(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchProduct(self.env['SEARCH_KEYWORD'])
        self.mp.clickSearchButton()
        self.sp.waitForSearchResultPage()
        self.sp.selectFirstItem()
        self.pp.waitForProductPage()
        self.pp.clickAddToCartButton()
        self.ex.waitForExtraoptionsPageContent()
        self.ex.waitForGoToCartButton()
        self.ex.goToCheckoutCart()
        self.scp.waitForCartPageContent()
        self.scp.setInputValue(self.value)
        self.scp.AssertProductNotAvailable()
# pytest --env=stage tests\test_add_to_cart.py
