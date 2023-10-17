from selenium import webdriver
import pytest
import allure
from allure_commons.types import AttachmentType
import os
from dotenv import load_dotenv, find_dotenv

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture(scope='session')
def env(request):
    load_dotenv(find_dotenv(f'.env.{request.config.getoption("--env")}'))
    env_variables = dict(os.environ)
    return env_variables

@pytest.fixture()
def setup(request, env):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.env = env
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()