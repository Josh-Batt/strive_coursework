import requests
#import json
from bs4 import BeautifulSoup as bs
#import datetime
import pandas as pd
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
#import seaborn as sns

def josh_scraper():

    path = requests.get("https://www.goodreads.com/book/show/13496.A_Game_of_Thrones")
    soup = bs(path.content, 'html.parser')

    num_ratings = soup.find('div', class = 'bookMeta')
    num_ratings = num_ratings.find('a')[1]

    num_ratings = num_ratings.find[0]

    return num_ratings

print(josh_scraper())