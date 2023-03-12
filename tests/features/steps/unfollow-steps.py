from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@given(u'clicks on a followed user')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/index")
    anchors = context.driver.find_elements(By.TAG_NAME, "a")

    for element in anchors:
        if element.text == "testuser2":
            testuser2 = element
    
    testuser2.click()

@when(u'the user clicks the unfollow button')
def step_impl(context):
    currentcountstring = context.driver.find_element(By.ID, "followParagraph").text.split(" ")
    global count
    count = int(currentcountstring[0])
    submit = context.driver.find_element(By.ID,"submit")
    submit.click()


@then(u'the user unfollows the other user')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")
    assert submit.get_attribute("value") == "Follow"


@then(u'the followers and following numbers of the users decrements by 1')
def step_impl(context):
    currentcountstring = context.driver.find_element(By.ID, "followParagraph").text.split(" ")
    count2 = int(currentcountstring[0])
    assert (count) == (count2 + 1)