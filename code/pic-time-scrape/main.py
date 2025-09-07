#! /Users/kevinlutzer/Projects/labs/code/pic-time-scrape/.venv/bin/python3

import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://leraeshawnphotography.pic-time.com/-kathydavid2/services.asmx/getUserRatedPhotosPercent"
data = requests.post(URL, {"projectId":40305341,"favoriteUserJobId":0,"photoCountPercent":0.15}, {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "pictimeProject": "AAAAABkBAABgMZ9-Wjr8D7Ar-PnYYi1PI7tHgUZj_70HBtegdJ7IHUPrBAPXq2qhI_55f9tCk34vOH3892v_32bDJJaInEpO_EJC4DNwKj8Iq7XUX6CVtg,,",
    "Cookie": "pictimeProject=AAAAABkBAABgMZ9-Wjr8D7Ar-PnYYi1PI7tHgUZj_70HBtegdJ7IHUPrBAPXq2qhI_55f9tCk34vOH3892v_32bDJJaInEpO_EJC4DNwKj8Iq7XUX6CVtg,,; pictimeGal40305341=6769ffef6f04dc0fc0c503ff; _gcl_au=1.1.825890912.1734816019; _ga_WFQFFZ86BQ=GS1.1.1734999896.3.1.1735000048.59.0.0; _ga=GA1.1.13257906.1734816019"
})

# Command to execute 
# Using Windows OS command 
cmd = 'notepad'
  
# Using os.system() method 
os.system(cmd).st



print(data.content)

# print(soup)