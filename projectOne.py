# Upwork Task 

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import selenium

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_data(): 
    master_list = []

    url = f"https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/quarterly-refunding-archives/quarterly-refunding-financing-estimates-by-calendar-year" 
    html = requests.get(url, "html.parser").text

    soup = bs(html, "html.parser")
    table = soup.find("table")

    years = table.find("thead").find_all("th", {"class": "span"})
    for year in years: 
      year = year.text
      master_list.append(year)

      data = table.find("thead").find_all("th", {"headers": f"{year}"})

      for info in data: 
        print(info.find("a").href) 
    
get_data()
