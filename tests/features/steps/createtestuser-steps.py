from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'the user is on the “Register” page')
def step_impl(context):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    context.driver.implicitly_wait(5)
    context.driver.get(ip + "auth/register")

@when(u'the user enters a valid username, valid email, valid password and confirms the password')
def step_impl(context):
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("wojcikm")
    email = context.driver.find_element(By.ID,"email")
    email.send_keys("wojcikm@uwindsor.ca")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("wojcikm")
    password2 = context.driver.find_element(By.ID,"password2")
    password2.send_keys("wojcikm")

@when(u'clicks the “Register” button')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()

@then(u'the user has now successfully created an account')
def step_impl(context):

    anchors = context.driver.find_elements(By.TAG_NAME, "h1")

    stringtest = ""

    for element in anchors:
        if element.text == "Two Factor Authentication":
            stringtest = element.text
    
    assert stringtest == "Two Factor Authentication"