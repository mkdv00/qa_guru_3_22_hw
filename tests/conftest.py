import os

import pytest
from dotenv import load_dotenv
from framework.demo_qa import DemoQaWithEnv
from selene.support.shared import browser

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(env):
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres


@pytest.fixture(scope='session')
def login_wia_api(demoshop):
    browser.config.base_url = os.getenv("PROD_DEMOQA")
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture(scope='module')
def browser_open(login_wia_api):
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": login_wia_api})

    yield browser

    browser.quit()
