from behave import Given, Then, When
import time
from behave import given, when, then
from behave.exception import StepNotImplementedError
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


@given('launch browser')
def launch_browser(context):
    context.driver = WebDriver()
    context.options = Options()


@when('open browser')
def openorange_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    time.sleep(5)


@then('enter un and pwd')
def verify(context):
    un = context.driver.find_element('xpath', '//input[@name="username"]').send_keys('Admin')
    pwd = context.driver.find_element('xpath', '//input[@name="password"]').send_keys("admin123")
    login_btn = context.driver.find_element('xpath',
                                            '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
    assert context.driver.find_element('xpath', "//h6[text()='Dashboard']").is_displayed()


@then('close page')
def close(context):
    context.driver.quit()
