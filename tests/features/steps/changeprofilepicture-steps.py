from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from currentip import ip

@given(u'on the "Profile" page')
def step_impl(context):
    context.driver.get(ip + "user/wojcikm")


@when(u'the user clicks the “Edit your profile” button')
def step_impl(context):
    editprofile = context.driver.find_element(By.ID,"editprofile")
    editprofile.click()
    context.driver.implicitly_wait(5)



@when(u'the user pastes a link to an imgur in the "Post the link" box')
def step_impl(context):
    photo = context.driver.find_element(By.ID,"profilePicture")
    photo.clear()
    photo.send_keys("https://preview.redd.it/myze2s70v5051.png?auto=webp&s=988c85b45884dc6ab51d81c7b1db2d06c49e8d52")
    context.driver.implicitly_wait(100)


@when(u'the user presses submit')
def step_impl(context):
    submit = context.driver.find_element(By.ID,"submit")
    submit.click()


@then(u'the users profile picture updates')
def step_impl(context):
    context.driver.get(ip + "user/wojcikm")
    source = context.driver.find_element(By.ID,"picture")
    assert source.get_attribute("src") == "https://preview.redd.it/myze2s70v5051.png?auto=webp&s=988c85b45884dc6ab51d81c7b1db2d06c49e8d52"