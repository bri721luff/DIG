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

# More Definitions
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

# Part 1 Renames downloaded file
fRA = ON
fRB = DL.replace('NewNews'+user+'.csv') #AKA News comes in

# Part 2 Defines More Terms
import pandas as pd
x = "No news is good news!"
y = "Check out your changes!"
RA = pd.read_csv('OldNews'+user+'.csv')
RB = pd.read_csv('NewNews'+user+'.csv')
# Interacts with data
c = pd.concat([RA,RB], axis=0)
c.drop_duplicates(keep=False, inplace=True)
# Prepares Report
c.reset_index(drop=True, inplace=True)
# Adds the weblink column
c["weblink"] = "https://www.openstreetmap.org/" + c["@type"].astype(str) + "/" + c["@id"].astype(str)
# Saves to file
c.to_csv('MostRecentResults'+user+'.csv')

# Part 2 New News becomes Old News
NN.replace('OldNews'+user+'.csv')

# Part 3 Making an Email Method
subject = "Check out your changes!"
body = "Thank you for using the OSMgaarten service. We hope this helps you make OSM great!"
sender_email = "brian.luff.1124@gmail.com"
receiver_email = "brian.luff.1124@gmail.com"
password = "Va1pa4a1s0!"
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails
# Add body to email
message.attach(MIMEText(body, "plain"))
filename = "MostRecentResults"+user+".csv"  # In same directory as script
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()
# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

# Check your inbox; See you tomorrow!