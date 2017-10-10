#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from time import sleep
import random

# Twitter credentials
CONSUMER_KEY = 'Your Consumer Key'
CONSUMER_SECRET = 'Your Consumer Secret Key'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Open text file and randomize lines
with open('prideandpred.txt', 'r') as book:
    unwanted_word = ("Mrs.", "Mr.")
    book_lines = book.read().split('.')
random.shuffle(book_lines)

# Get random line
def tweeter():
    for line in book_lines:
        print line,
        if line != '\n' or unwanted_word not in line:
            try:
                api.update_status(line + ". #PrideandPrejudice")
                time.sleep(900)  # Tweet every 15 min
            except Error as tweety_error:
                print "Encountered tweety error: "
                print tweety_error

tweeter()

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


