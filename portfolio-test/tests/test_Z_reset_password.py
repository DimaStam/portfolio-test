import pytest
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.UserAccountPage import UserAccountPage
import allure

@pytest.mark.usefixtures('setup')
class Test_Reset_Password:

    @allure.title('Test zmiany hasła używtkownika')
    def test_reset_password(self):
        print(self.env)
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.uap = UserAccountPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.clickAcceptCookies()
        self.lp.clickAccountIcon()
        self.lp.waitForLoginPage()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['PASSWORD'])
        self.lp.clickLoginButton()
        self.uap.waitForUserAccountContent()
        self.uap.AssertHappyPass()
        self.uap.clickAccountData()
        self.uap.clickResetPassword()
        self.uap.setUserActualPassword(self.env['PASSWORD'])
        self.uap.setUserNewPassword(self.env['NEW_PASSWORD'])
        self.uap.setConfirmUserNewPassword(self.env['NEW_PASSWORD'])
        self.uap.clickSaveButton()
        self.uap.waitForSeccessMessage()
        self.uap.AssertPasswordChanged()

    @allure.title('Test prawidłowego logowania po zmianie hasła')
    def test_login_with_new_wassword(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.uap = UserAccountPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.clickAcceptCookies()
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['NEW_PASSWORD'])
        self.lp.clickLoginButton()
        self.uap.waitForUserAccountContent()
        self.uap.AssertHappyPass()

    @allure.title('Test logowania używając stare hasło')
    def test_login_old_password(self):
        # pytest.skip()
        self.driver.get(self.env['URL'])
        self.mp = MainPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.mp.waitForMainPage()
        self.mp.clickAcceptCookies()
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.env['USERNAME_1'])
        self.lp.setUserPassword(self.env['PASSWORD'])
        self.lp.clickLoginButton()
        self.lp.waitForAlertMessage()
        self.lp.AssertUnhappyPass()