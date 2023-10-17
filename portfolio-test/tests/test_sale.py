import pytest
import pandas as pd
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.SummaryPage import SummaryPage
from pages.ExtraoptionsPage import ExtraoptionsPage
from pages.CheckoutDeliveryPage import CheckoutDeliveryPage
from pages.CreateAccountPage import CreateAccountPage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
import allure

@pytest.mark.usefixtures('setup')
class Test_Sale:
    
    @allure.title('Test sprzedaży Kurier DHL + PayU dla niezalogowanego użytkownika')
    def test_courier_dhl_payU(self):
        # pytest.skip()
        self.driver.get(self.env['PRODUCT_URL'])
        self.mp = MainPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.sump = SummaryPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.cdp = CheckoutDeliveryPage(self.driver)
        self.cap = CreateAccountPage(self.driver)
        self.pp.waitForProductPage()
        self.mp.clickAcceptCookies()
        self.pp.clickAddToCartButton()
        self.ex.waitForExtraoptionsPageContent()
        self.ex.goToCheckoutCart()
        self.scp.waitForCartPageContent()
        self.scp.goToCheckoutDelivery()
        self.lp.waitForLoginPage()
        self.cap.clickContinueAsGuest()
        self.cdp.waitForCheckutAdressForm()
        self.cdp.setEmail(self.env['EMAIL'])
        self.cdp.setPhoneNumber(self.env['PHONE'])
        self.cdp.setFirstName(self.env['NAME'])
        self.cdp.setLastName(self.env['LASTNAME'])
        self.cdp.setStreet(self.env['STREET'])
        self.cdp.setPostcode(self.env['POSTCODE'])
        self.cdp.setCity(self.env['CITY'])
        self.cdp.waitForDeliмeryMethodsBlock()
        self.cdp.clickCourierDHL()
        self.cdp.goToCheckoutSummary()
        self.sump.waitForCheckoutSummaryPageContent()
        self.sump.selectPayU()
        self.sump.clickCheckbox1()
        self.sump.clickOrderAndPayButton()
        self.sump.waitForPayUPaymentPage()
        self.sump.AssertPayUTitle()