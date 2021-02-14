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
import time
from pathlib import Path
import pandas as pd

# Part 1
# Definitions
user = 'VLD168'
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
time.sleep(45)
driver.close()

# Part 2
# Definitions
fWA = 'OldNews'+user+'.csv' #Filepath of second DL file in chain
fWB = 'NewNews'+user+'.csv' #Filepath of first DL file in chain
fWC = 'C:\\Users\\Brian\\Downloads\interpreter' #Filepath of current DL file, does not come with suffix
fWD = 'LeastRecent'+user+'Results.csv' #Filepath of old report
fWE = 'MostRecent'+user+'Results.csv' #Filepath of newest report
ON = Path(fWA)
NN = Path(fWB)
DL = Path(fWC)
LR = Path(fWD)
MR = Path(fWE)
# Defines dataframe
fRA = ON
# Renames downloaded file and defines dataframe
fRB = DL.replace('NewNews'+user+'.csv')

# Preps csv's
RA = pd.read_csv('OldNews'+user+'.csv')
RB = pd.read_csv('NewNews'+user+'.csv')
# Interacts with data
a = pd.concat([RA,RB], axis=0)
a.drop_duplicates(keep=False, inplace=True)
# Prepares Report
a.reset_index(drop=True, inplace=True)
# Adds the weblink column
a["weblink"] = "https://www.openstreetmap.org/" + a["@type"].astype(str) + "/" + a["@id"].astype(str)
# Saves to file
a.to_csv('MostRecentResults'+user+'.csv')
# Changes NewNews to OldNews
NN.replace('OldNews'+user+'.csv')
#This is where it switches to DIG2