#!/usr/bin/env python
# coding: utf-8

# Part 1 Script Packages
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Part 2 Script Packages
import os
import time
import pathlib
from pathlib import Path
import pandas as pd

# Part 3 Script Packages
import smtplib
import datetime as dt
import time
import email
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Part 1 Definitions
user = VLD168
chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\dev-app2")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
# Gets Overpass API
driver.get('https://lz4.overpass-api.de/query_form.html')
# Waits for it to load
driver.implicitly_wait(1000)
# Enters query into field and returns file
actions = ActionChains(driver)
form = driver.find_element_by_xpath("//form/p/textarea[@name='data']")
actions.move_to_element(to_element=form).click().perform()
actions.send_keys('[out:csv(::id,::type,::user,::timestamp;true;",")];nwr(user:'+user+');out meta;\ue004\ue006').click().perform()    
