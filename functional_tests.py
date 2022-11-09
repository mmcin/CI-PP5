"""
Need to add site title to assert
"""

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert '' in browser.title