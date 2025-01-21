# coding: utf-8

import os
import sys

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

from datetime import datetime, time



def convert_to_datetime(timestamp):
    # Convert Unix timestamp to datetime object
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object

def crawl_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
    else:
        return None

def main():
    url = 'https://www.google.com'
    title = crawl_webpage(url)
    if title:
        return title
    else: 
        return "No title found"


if __name__ == '__main__':
    main()

