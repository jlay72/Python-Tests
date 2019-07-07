import unittest
import subprocess
from selenium import webdriver
import sys
import os
os.chdir(os.path.dirname(sys.argv[0]))
import configparser
import pytest
import allure_pytest
import allure
import urllib
import webbrowser
#thisfolder = os.path.dirname(os.path.abspath(__file__))
#initfile = os.path.join(thisfolder, "config.ini")
from py._builtin import execfile
import random
import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Test_test1(unittest.TestCase):

    def test_google_check(driver):

        #Open Google Front Page
        webbrowser.open("https://www.google.com/")
        time.sleep(5)
        
    def test_select_search_field(driver):

        #Select Search field 
        search_option = driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input")
        search_option()
        
    def test_enter_data(driver):

        # Enter Company in Company Name field
        password = driver.find_element_by_class_name("col-md-6")
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(password)
        actions.click()
        actions.send_keys(random.choice(mylist))# Replace with whichever keys you want.
        actions.perform()
