from behave import *
from behave.exception import StepNotImplementedError
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep


@given('launch webdrive')
def step_impl(context):
    context.driver = WebDriver()

@when('lauch App')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('Enter un "{un}" and "{pwd}"')
def step_impl(context, un, pwd):
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(
        un)
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(
        pwd)
    sleep(2)


@when('click login')
def step_impl(context):
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    sleep(5)


@then(u'successfull login Dashboard')
def step_impl(context):
    try:
        details = context.driver.find_element('xpath', '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    except Exception as e:
        print(e, 'is An Error')
        context.driver.quit()
        assert False, "Test Case Failed"
    else:
        if details == "Dashboard":
            context.driver.quit()
            assert True, "Test Case Passed"


@then(u'Admin module')
def step_impl(context):
    context.driver.find_element('xpath', '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
    sleep(2)


@then(u'Admin dashboard')
def step_impl(context):
    status = context.driver.find_element('xpath',
                                         '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]').is_displayed()
    assert status


@then(u'Directory module')
def step_impl(context):
    context.driver.find_element('xpath', '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').click()
    sleep(2)


@then(u'Directory dashboard')
def step_impl(context):
    state = context.driver.find_element('xpath',
                                        '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').is_displayed()
    assert state
