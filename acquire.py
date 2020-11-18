# Acquire File
# Imports

import pandas as pd
import numpy as np
from requests import get
from os import path
from bs4 import BeautifulSoup

################## Acquire OpenCV Repo Data ##################
def get_repo_data():
    ''' 
    
    '''
  
    return df


################## Acquire Helper Functions ##################
def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML returning a soup object.
    '''
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_all_urls():
    '''
    This function scrapes all of the OpenCV repo urls from the Github and returns a list of urls.
    '''
    # The base url for the main Codeup blog page
    url = '            '
    
    # Make request and soup object using helper
    soup = make_soup(url)
    
    # Create a list of the anchor elements that hold the urls.
    urls_list = soup.find_all('a', class_='jet-listing-dynamic-link__link')
    
    # I'm using a set comprehension to return only unique urls because list contains duplicate urls.
    urls = {link.get('href') for link in urls_list}

    # I'm converting my set to a list of urls.
    urls = list(urls)
        
    return urls