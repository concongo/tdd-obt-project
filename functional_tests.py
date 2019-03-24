''' This File has been created to Test Django Installation at first '''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver #
# Reference

browser = webdriver.Chrome(executable_path='./utils/chromedriver') # Using Chrome browser instead
browser.get('http://localhost:8000')

assert 'Django' in browser.title # This is to check if the basic django server is upexit
