import os

import allure
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()


def test_login_with_api(browser_open):
    browser.open("/")

    with allure.step("Verify successful authorization"):
        browser.element(".account").should(have.text(os.getenv("LOGIN")))


def test_search_negative_result(browser_open):
    browser.open("/")

    with allure.step("Negitive search"):
        browser.element('.search-box [value="Search store"]').click()
        browser.element('.search-box [value="Search store"]').type('negative test').press_enter()
        browser.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_watch_profile(browser_open):
    browser.open("/")

    with allure.step("Check info in profile"):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('#FirstName').should(have.value('mkdv'))
        browser.element('#LastName').should(have.value('00'))
        browser.element('#Email').should(have.value(os.getenv('LOGIN')))
        browser.element('[checked="checked"]#gender-male')


def test_watch_page_change_password(browser_open):
    browser.open("/")

    with allure.step("Check text buttion in change password"):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('[href="/customer/changepassword"]').should(have.text('Change password')).click()
        browser.element('[for="OldPassword"]').should(have.text('Old password:'))
        browser.element('[for="NewPassword"]').should(have.text('New password:'))
        browser.element('[for="ConfirmNewPassword"]').should(have.text('Confirm password:'))


def test_logout(browser_open):
    browser.open("/")

    with allure.step("Check logout"):
        browser.element('.ico-logout').click()
        browser.element('.ico-login').should(have.text('Log in'))
