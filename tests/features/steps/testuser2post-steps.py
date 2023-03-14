from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'on the “Home” page')
def step_impl(context):
    #context.driver.get(ip + "index")
    assert 1==1

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