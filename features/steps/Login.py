from behave import given, when, then
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys


@given("launch webdriver")
def launch_webdriver(context):
    context.driver = WebDriver()
    context.option = Options()


@when("open orange hrm login")
def launch_orange_hrm(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@when('orange hrm "{un}" and "{pwd}"')
def un_pwd(context, un, pwd):
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(
        un)
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(
        pwd)
    sleep(2)


@when("click login button")
def login(context):
    context.driver.find_element('xpath',
                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    sleep(5)


@then("login successfully")
def successfully(context):
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
