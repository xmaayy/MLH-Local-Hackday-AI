import markovify
import config
import random
from mlh_twitter_api import get_user_tweets as fetch
from twitter_scraper_fetcher import *
import re


# remove emoji, punctuation, urls from tweets
def create_string(tweets):
    text = ""

    for tweet in tweets:
        text += (
            tweet + "\n\n"
        )  # Make sure each tweet is handled properly by markovify
    return text


def generate_bot_answer_with_text_model(text_model, user_question,
        twitter_handle):
    bot_answer = None
    
    word_list = user_question.split(" ")
    random_word = random.choice(word_list)
    bot_answer = text_model.make_sentence_with_start(
        random_word, strict=False)
    print("We cool")
    return bot_answer



      
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    tweets = get_user_tweets(twitter_handle)
    clean_tweets = clean_tweets_data(tweets)
    text = "".join(map(str, clean_tweets))
    text_model = markovify.Text(text)