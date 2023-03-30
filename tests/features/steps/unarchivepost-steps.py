from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'the user has archived posts')
def step_impl(context):
    context.driver.get(ip + "archivedposts")
    unarchivebutton = context.driver.find_element(By.ID,"unarchive")


@when(u'the user clicks on the "unarchive" button')
def step_impl(context):
    unarchivebutton = context.driver.find_element(By.ID,"unarchive")
    unarchivebutton.click()
    context.driver.implicitly_wait(5)


@then(u'the review should be removed from the user\'s archived posts')
def step_impl(context):
    context.driver.get(ip + "archivedposts")
    elements = context.driver.find_elements(By.TAG_NAME,"table")
    if(len(elements) == 0):
        context.driver.get(ip + "explore")
    else:
        raise NotImplementedError(u'STEP: Then the review should be removed from the user\'s archived posts') 


