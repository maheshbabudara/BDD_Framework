import time
from behave import given, when, then
from behave.exception import StepNotImplementedError
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


@given('launch chrome browser')
def step_impl(context):
    context.driver = WebDriver()
    context.options = Options()


@when('open orangehrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    time.sleep(5)


@then('verify that logo present or not')
def step_impl(context):
    status = context.driver.find_element('xpath',
                                         '//img[@src="/web/images/ohrm_branding.png?v=1721393199309"]').is_displayed()
    assert status == True


@then('close browser')
def step_impl(context):
    context.driver.quit()
# import time
#
# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
#
# @given('launch chrome browser')
# def step_impl(context):
#     options = Options()
#     context.driver = webdriver.Chrome(options=options)
#
# @when('open orangehrm homepage')
# def step_impl(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(10)
#     time.sleep(5)
# @then('verify that logo present or not')
# def step_impl(context):
#     try:
#         status = context.driver.find_element('xpath', '//img[@src="/web/images/ohrm_branding.png?v=1721393199309"]').is_displayed()
#         assert status==True
#     except NoSuchElementException:
#         assert False, "Logo not found"
#
# @then('close browser')
# def step_impl(context):
#     context.driver.quit()
