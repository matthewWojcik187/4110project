from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@given(u'enters their username,password, and incorrect two factor token')
def step_impl(context):
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("wojcikm")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("wojcikm")
    token = context.driver.find_element(By.ID,"token")
    token.send_keys("123456")


@then(u'the user is not logged in')
def step_impl(context):
    header = context.driver.find_elements(By.TAG_NAME,"h1")
    assert  header[0].text == "Sign In"
    