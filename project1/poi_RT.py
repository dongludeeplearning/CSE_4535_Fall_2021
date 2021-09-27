'''
@author: Lu Dong
Institute: University at Buffalo
'''
import json
import pandas as pd
from twitter import Twitter
from tweet_preprocessor import TWPreprocessor
from indexer import Indexer

# deal with retweet
# test_code
#jobs -l
twitter = Twitter()
#key="quarente"
poi = "JoeBiden"
raw_tweets = twitter.get_tweets_by_poi_screen_name(poi,"en",100)
# keyword_search=twitter.get_tweets_by_lang_and_keyword(key,"en",5)
## reply_tweets= twitter.get_replies(tweet, n)
# for twt in raw_tweets:
#     #print(twt.full_text)
#     print(TWPreprocessor.preprocess_poi(twt))
# for tweet in keyword_search:
#     print(TWPreprocessor.preprocess_keyword(tweet))
