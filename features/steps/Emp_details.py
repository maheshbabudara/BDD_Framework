from behave import given, when, then
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from time import sleep


@given("launch")
def launch(context):
    context.driver = WebDriver()
    context.options = Options()

@when("open webpage")
def webpage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    sleep(2)

@then("Enter Employee records")
def automate(context):
    context.driver.find_element("xpath",'//input[@name="username"]').send_keys("Admin")
    context.driver.find_element("xpath",'//input[@name="password"]').send_keys("admin123")
    context.driver.find_element('xpath','//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
    sleep(1)
    context.driver.find_element('xpath',"//span[text()='Directory']").click()
    sleep(1)
    context.driver.find_element('xpath','//input[@placeholder="Type for hints..."]').send_keys("Robert  Stewart")
    sleep(1)
    context.driver.find_element('xpath','//label[text()="Job Title"]/../../div[2]/div/div/div[@class="oxd-select-text-input"]').send_keys('Automaton Tester')
    sleep(1)
    # context.driver.find_element('xpath',"//label[text()='Job Title']/../../div[2]/div/div/div[text()='Automaton Tester']").click()
    sleep(1)
    context.driver.find_element('xpath','//label[text()="Location"]/../../div[2]/div/div/div[@class="oxd-select-text-input"]').send_keys('HQ - CA, USA')
    sleep(1)
    # context.driver.find_element('xpath','//label[text()="Location"]/../../div[2]/div/div/div[text()="Texas R&D"]').click()
    sleep(2)
    context.driver.find_element('xpath',"//button[contains(text(),'Search')]").click()
    sleep(2)
    assert context.driver.find_element('xpath',"//span[text()='No Records Found']").is_displayed()

@then("close webpage")
def close(context):
    context.driver.quit()


