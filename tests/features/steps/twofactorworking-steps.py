from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'the user is on the login page')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    context.driver.implicitly_wait(5)
    context.driver.get(ip)


@given(u'enters their username,password, two factor token')
def step_impl(context):
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("wojcikm")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("wojcikm")
    token = context.driver.find_element(By.ID,"token")
    token.send_keys("642342")


@when(u'the user presses sign in')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()


@then(u'the user is logged in')
def step_impl(context):
    context.driver.get(ip + "index")