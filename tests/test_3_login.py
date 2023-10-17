import pytest
import allure
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.ExtraoptionsPage import ExtraoptionsPage
from pages.CheckoutDeliveryPage import CheckoutDeliveryPage
from pages.CreateAccountPage import CreateAccountPage
from pages.UserAccountPage import UserAccountPage

@pytest.mark.usefixtures('setup')
class TestLogin:
    @allure.title('Test prawidłowego logowania')
    def test_login_passed(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.lp = LoginPage(self.driver)
        self.cap = CreateAccountPage(self.driver)
        self.mp = MainPage(self.driver)
        self.uap = UserAccountPage(self.driver)
        self.mp.waitForMainPage()
        self.lp.clickAccountIcon()
        self.lp.waitForLoginPage()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['PASSWORD'])
        self.lp.clickLoginButton()
        self.uap.waitForUserAccountContent()
        self.uap.AssertHappyPass()

    @allure.title('Test nieprawidłowego logowania')
    def test_login_failed(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.cap = CreateAccountPage(self.driver)
        self.uap = UserAccountPage(self.driver)
        self.mp.waitForMainPage()
        self.lp.clickAccountIcon()
        self.lp.waitForLoginPage()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['FAKE_PASSWORD'])
        self.lp.clickLoginButton()
        self.lp.waitForAlertMessage()
        self.lp.AssertUnhappyPass()

    @allure.title('Test logowania na checkoucie')
    def test_checkout_login(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.cdp = CheckoutDeliveryPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.SearchProduct(self.env['SEARCH_KEYWORD'])
        self.mp.clickSearchButton()
        self.sp.selectFirstItem()
        self.pp.clickAddToCartButton()
        self.ex.goToCheckoutCart()
        self.scp.goToCheckoutDelivery()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['PASSWORD'])
        self.lp.clickLoginButton()
        self.cdp.AssertCheckoutDeliveryTitle()
# pytest --env=stage tests\test_3_login.py
# pytest --env=stage tests\test_3_login.py::TestLogin::test_checkout_login
