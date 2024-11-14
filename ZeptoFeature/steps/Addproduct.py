import allure
from allure_commons.types import AttachmentType
from behave.exception import StepNotImplementedError
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys, ActionChains
from time import sleep
import os

location = os.getcwd()


@given(u'launch browser')
def step_impl(context):
    context.driver = WebDriver()
    context.option = Options()
    preferences = {'download.default_directory': location, 'plugins.always_open_pdf_externally': True}
    context.option.add_experimental_option("prefs", preferences)
    context.option.add_argument("--disable-Notifications")
    context.option.add_experimental_option("detach", True)
    context.option.add_argument("--headless")
    context.option.add_argument("--disable-gpu")


@when(u'open zepto')
def step_impl(context):
    context.driver.get("https://www.zeptonow.com/")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@when(u'Enter UN and PWD')
def step_impl(context):
    context.driver.find_element('xpath', "//span[text()='login']").click()
    sleep(2)
    context.driver.find_element('xpath', '//input[@placeholder="Enter Phone Number"]').send_keys('8639563301')
    sleep(2)
    context.driver.find_element('xpath', "//div[text()='Continue']").click()
    sleep(15)

@then(u'Add product')
def step_impl(context):
    sleep(5)
    context.driver.find_element('xpath','//div[@class="inline-block flex-1"]/a/span[@class="flex flex-1 items-center gap-x-1 text-md font-extralight text-gray-700"]/span[text()="Search for"]').click()
    sleep(2)
    context.driver.find_element('xpath',
                                '//input[@placeholder="Search for over 5000 products"]').send_keys('chocolate')
    sleep(2)
    context.driver.find_element('xpath', "//span[contains(text(),'cadbury ')]").click()
    sleep(2)
    context.driver.find_element('xpath',
                                "//h5[text()='Cadbury Celebrations Rich Dry Fruit Collection Chocolate Diwali Gift Pack']/../../../div[@class='relative mt-12 px-1.5']/button/div/span[text()='Add to Cart']").click()
    sleep(2)
    context.driver.find_element('xpath', "//span[text()='Cart']").click()
    sleep(2)
    condition = context.driver.find_element('xpath',
                                            "//p[text()='Cadbury Celebrations Rich Dry Fruit Collection Chocolate Diwali Gift Pack']").is_displayed()
    sleep(2)
    if condition == False:
        allure.attach(context.driver.get_screenshot_as_png(), name="Addtocart.png", attachment_type=AttachmentType.PNG)
    assert condition
