from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@when(u'the user clears the "Post the link" box')
def step_impl(context):
    photo = context.driver.find_element(By.ID,"profilePicture")
    photo.clear()


@then(u'the users profile picture returns to the default')
def step_impl(context):
    context.driver.get(ip + "user/wojcikm")
    source = context.driver.find_element(By.ID,"picture")
    text = source.get_attribute("src") 
    assert text.find("https://www.gravatar.com/avatar/") != -1