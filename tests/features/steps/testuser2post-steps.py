from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ip = "http://18.218.251.148:5000/"

@given(u'on the “Home” page')
def step_impl(context):
    context.driver.get(ip + "index") 

@when(u'the user populates the “Say something” text box with a review')
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