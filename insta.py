#import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#import self modules
from check_load import *
from get_creds import *

def init_browser():
    if  platform.system() == "Windows":
        browser = webdriver.Firefox(executable_path=(os.getcwd() + '/geckodriver/geckodriver.exe'))
        return browser
    elif platform.system() == "Linux":
        browser = webdriver.Firefox(executable_path=(os.getcwd() + '/geckodriver/geckodriver'))
        return browser

def login_insta(browser):
    browser.get("https://www.instagram.com/")
    sleep(2)
    
    browser.implicitly_wait(30)
    username = browser.find_element_by_name('username')
    username.send_keys(USERNAME)
    browser.implicitly_wait(30)
    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)
    sleep(2)
    
    # Click the login button
    browser.implicitly_wait(30)
    browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
    browser.implicitly_wait(30)
    
    #Save Info, Not Now
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    browser.implicitly_wait(30)
    
    browser.find_element_by_xpath("/html/body/div/div/div/div//div[3]/button[2]").click()
    browser.implicitly_wait(30)
    
def search_user(browser):
    search_user = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div[2]/[@value='']")
    search_user.send_keys(SEARCH_USER)
    browser.implicitly_wait(30)
    
    
if __name__ == "__main__":
    check_load()
    browser = init_browser()
    login_insta(browser)