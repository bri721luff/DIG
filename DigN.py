#!/usr/bin/env python
# coding: utf-8
# Part 1 Script Packages
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# Part 2 Script Packages
import time
import pathlib
from pathlib import Path
import pandas as pd
# Part 3 Script Packages
from pathlib import Path
from datetime import date
import pandas as pd
# Part 1
# Definitions
user_names = ['Always_Dreamin', 'WhiteIndigo', 'StargazingViolet', 'LagunaBlue']
for user in user_names:
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
    fWA = 'News\\OldNews{0}.csv'.format(user)  #Filepath of second DL file in chain
    fWB = 'News\\NewNews{0}.csv'.format(user)  #Filepath of first DL file in chain
    fWC = 'C:\\Users\\Brian\\Downloads\interpreter' #Filepath of current DL file, does not come with suffix
    fWD = 'Results\\LeastRecent{0}Results.csv'.format(user)  #Filepath of old report
    fWE = 'Results\\MostRecent{0}Results.csv'.format(user)  #Filepath of newest report
    ON = Path(fWA)
    NN = Path(fWB)
    DL = Path(fWC)
    LR = Path(fWD)
    MR = Path(fWE)
# Renames downloaded file and defines dataframe
    fRB = DL.replace('News\\NewNews{0}.csv'.format(user))
# Defines dataframe
    fRA = ON
# Preps csv's
    RA = pd.read_csv('News\OldNews'+user+'.csv')
    RB = pd.read_csv('News\\NewNews{0}.csv'.format(user))
# Combines lists and drops duplicates
    a = pd.concat([RA, RB], axis=0)
    a.drop_duplicates(keep=False, inplace=True)
# Prepares Report
    a.reset_index(drop=True, inplace=True)
# Adds the weblink column
    a["weblink"] = "https://www.openstreetmap.org/" + a["@type"].astype(str) + "/" + a["@id"].astype(str)
# Saves to file
    a.to_csv('Results\MostRecentResults'+user+'.csv')
# Changes NewNews to OldNews
    NN.replace('News\OldNews'+user+'.csv')
    time.sleep(3)
# Part 3
# Definitions
    today = date.today()
    fC = 'Results\LeastRecentResults'+user+'.csv'  # Filepath of old report
    fD = 'Results\MostRecentResults'+user+'.csv'  # Filepath of newest report
    fE = 'Results\MasterResults'+user+'.csv'  # Filepath
    LR = Path(fC)
    MR = Path(fD)
    MM = Path(fE)
# opens the results as dataframe
    aa = pd.read_csv(MR)
# modifies dataframe to filter out today's changes
    bb = aa[~aa["@timestamp"].str.contains("{0}".format(today))]
# creates the filtered results csv
    bb.to_csv(LR)
# Preps csv's
    AA = pd.read_csv(MR)
    BB = pd.read_csv(LR)
# combines dataframes to produce master dataframe
    cc = pd.concat([AA, BB], axis=0)
    cc.drop_duplicates(keep=True, inplace=True)
# Prepares Report
    cc.reset_index(drop=True, inplace=True)
# Creates/overwrites master csv
    cc.to_csv(MM)
