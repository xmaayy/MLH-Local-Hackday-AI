import requests
from bs4 import BeautifulSoup
import re

CONTENT_CLASS_NAME = "TweetTextSize"
CONTENT_CONTAINER_TAGS = ["p"]
EMPTY_ITEMS = [None, " ", "None"]
TWITTER_URL = "https://twitter.com/"

emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )


def get_elements(twitter_handle: str):
    """
    Add some comments to make sense of what you're doing
    """
    url = TWITTER_URL + twitter_handle
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")

    return soup.find_all(CONTENT_CONTAINER_TAGS, 	attrs={"class": CONTENT_CLASS_NAME})
    

def get_user_tweets(twitter_handle):
    elements = get_elements(twitter_handle)
    tweets = []
    for post in elements:
        for text in post.contents:
            # Check if line contains actual text
            if text.string not in EMPTY_ITEMS:
                tweets.append(text.string)
    return tweets


def clean_tweets_data(tweets):
    ## Nothing here yet!
    pass
    
  
            
                

    
