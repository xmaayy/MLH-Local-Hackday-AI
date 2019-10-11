import requests
from bs4 import BeautifulSoup
import re

CONTENT_CLASS_NAME = "TweetTextSize"
CONTENT_CONTAINER_TAGS = ["p"]
EMPTY_ITEMS = [None, " ", "None"]
TWITTER_URL = "https://twitter.com/"


def get_elements(twitter_handle):
    url = TWITTER_URL + twitter_handle
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")

    return soup.find_all(CONTENT_CONTAINER_TAGS, 	attrs={"class": CONTENT_CLASS_NAME})
    
def get_user_tweets(twitter_handle):
  ## Nothing here yet!
  pass

def clean_tweets_data(tweets):
  ## Nothing here yet!
  pass
    
  
            
                

    
