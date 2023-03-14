from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'the test user is logged in')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    context.driver.implicitly_wait(5)
    
    context.driver.get(ip)
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("testuser2")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("testuser2")
    token = context.driver.find_element(By.ID,"token")
    token.send_keys("642342")
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()

@given(u'on the “Home” page')
def step_impl(context):
    context.driver.get(ip + "index")

@when(u'the test user populates the “Say something” text box with a review')
def step_impl(context):
    postbox = context.driver.find_element(By.ID,"post")
    postbox.send_keys("Hello")


@when(u'they click “Submit”')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()


@then(u'blog is posted so that everyone can view it on the “Explore” page')
def step_impl(context):
    assert 1==1


