from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@given(u'the user is logged in')
def open_browser(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    context.driver.implicitly_wait(5)
    
    context.driver.get("http://3.144.24.185:5000")
    username = context.driver.find_element(By.ID,"username")
    username.send_keys("wojcikm")
    password = context.driver.find_element(By.ID,"password")
    password.send_keys("wojcikm")
    token = context.driver.find_element(By.ID,"token")
    token.send_keys("642342")
    submit = context.driver.find_element(By.ID,"submit")   
    submit.click()


@given(u'on the “Explore” page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/explore")
    


@when(u'the user clicks the “favorite” button')
def step_impl(context):
    archivebutton = context.driver.find_element(By.ID,"archive")
    archivebutton.click()
    context.driver.implicitly_wait(5)
    


@then(u'the post is put in their archive')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/archivedposts")
    unarchivebutton = context.driver.find_element(By.ID,"unarchive")
    
    
