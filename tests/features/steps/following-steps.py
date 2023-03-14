from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'clicks on another user profile')
def step_impl(context):
    context.driver.get(ip + "explore")
    anchors = context.driver.find_elements(By.TAG_NAME, "a")

    for element in anchors:
        if element.text == "testuser2":
            testuser2 = element
    
    testuser2.click()


@when(u'the user clicks the follow button')
def step_impl(context):
    currentcountstring = context.driver.find_element(By.ID, "followParagraph").text.split(" ")
    global count
    count = int(currentcountstring[0])
    submit = context.driver.find_element(By.ID,"submit")
    submit.click()


@then(u'the user is following the other user')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")
    assert submit.get_attribute("value") == "Unfollow"


@then(u'the followers and following numbers of the users increments by 1')
def step_impl(context):
    currentcountstring = context.driver.find_element(By.ID, "followParagraph").text.split(" ")
    count2 = int(currentcountstring[0])
    assert (count+1) == count2