from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ip = "http://18.218.251.148:5000/"

@given(u'the user is on the “Sign in” page')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    context.driver.implicitly_wait(5)
    context.driver.get(ip)

@when(u'the user enters their username with a corresponding password and token')
def step_impl(context):
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("testuser2")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("testuser2")
    token = context.driver.find_element(By.ID,"token")
    token.send_keys("642342")

@then(u'clicks the “sign in” button')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()
