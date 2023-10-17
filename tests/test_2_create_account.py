import pytest
import allure
from pages.CreateAccountPage import CreateAccountPage
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.ExtraoptionsPage import ExtraoptionsPage
from pages.LoginPage import LoginPage
from pages.UserAccountPage import UserAccountPage

@pytest.mark.usefixtures('setup')
class TestCreateAccount:

    @allure.title('Test rejestracji użytkownika')
    def test_create_account(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.cap = CreateAccountPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.uap = UserAccountPage(self.driver)
        self.mp.waitForMainPage()
        self.cap.clickAccountIcon()
        self.lp.waitForLoginPage()
        self.cap.clickCreateAccountButton()
        self.cap.waitForCreateAccountForm()
        self.cap.setName(self.env['NAME'])
        self.cap.setUserLastname(self.env['LASTNAME'])
        self.cap.setEmail(self.env['USERNAME_1'])
        self.cap.setUserPassword(self.env['PASSWORD'])
        self.cap.setUserPasswordConf(self.env['PASSWORD'])
        self.cap.clickSighInButton()
        self.uap.waitForUserAccountContent()
        self.cap.AssertRegistrationSuccess()

    @allure.title('Test rejestracji na checkoucie')
    def test_checkout_create_account(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.cap = CreateAccountPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.uap = UserAccountPage(self.driver)
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
        self.scp.goToCheckoutDelivery()
        self.cap.clickCreateAccountButton()
        self.cap.waitForCreateAccountForm()
        self.cap.setName(self.env['NAME'])
        self.cap.setUserLastname(self.env['LASTNAME'])
        self.cap.setEmail(self.env['USERNAME_2'])
        self.cap.setUserPassword(self.env['PASSWORD'])
        self.cap.setUserPasswordConf(self.env['PASSWORD'])
        self.cap.clickSighInButton()
        self.cap.AssertRegistrationSuccess()
# pytest --env=stage tests\test_2_create_account.py
