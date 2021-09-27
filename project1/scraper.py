'''
@author: Souvik Das
Institute: University at Buffalo
'''

import json
import pandas as pd
from twitter import Twitter
from tweet_preprocessor import TWPreprocessor
from indexer import Indexer

#reply_collection_knob = False
reply_collection_knob = True


def read_config():
    with open("config.json", 'r') as json_file:
        data = json.load(json_file)

    return data


def write_config(data):
    with open("config.json", 'w') as json_file:
        json.dump(data, json_file)


def save_file(data, filename):
    df = pd.DataFrame(data)
    df.to_pickle("data/" + filename)


def read_file(type, id):
    return pd.read_pickle(f"data/{type}_{id}.pkl")


# get reply
def get_replies(tweet):
    tweet_id = tweet.id
    name = tweet.user.screen_name
    max_id = None
    replies = tweepy.Cursor(api.search, q='to:'+name,
                                since_id=tweet_id, max_id=max_id, result_type='recent',tweet_mode='extended').items(10)

    return replies

def main():
    config = read_config()
    indexer = Indexer()
    twitter = Twitter()

    pois = config["pois"]
    keywords = config["keywords"]

    # print(len(pois))
    # print(len(keywords))
    #print(keywords[1]["name"])

    for i in range(len(pois)):
        if pois[i]["finished"] == 0:
            print(f"---------- collecting reply_tweets for poi: {pois[i]['screen_name']}")
            screen_name=pois[i]['screen_name']
            type=pois[i]['lang']
            N=500
            raw_tweets = twitter.get_tweets_by_poi_screen_name(screen_name,type,N)  # pass args as needed

            processed_tweets = []
            for tw in raw_tweets:
                processed_tweets.append(TWPreprocessor.preprocess_poi(tw))

            indexer.create_documents(processed_tweets)

            pois[i]["finished"] = 1
            pois[i]["collected"] = len(processed_tweets)

            write_config({
                "pois": pois, "keywords": keywords
                })

            #save_file(processed_tweets, f"poi_{pois[i]['id']}.pkl")
            save_file(processed_tweets, f"poi_{i}.pkl")
            print("------------ process complete -----------------------------------")

        #if reply_collection_knob:



    for i in range(len(keywords)):
       if keywords[i]["finished"] == 0:
            #print(i)
            print(f"---------- collecting tweets for keyword: {keywords[i]['name']}")
            key = keywords[i]['name']
            type= keywords[i]['lang']
            N=1000

            raw_tweets = twitter.get_tweets_by_lang_and_keyword(key,type,N)  # pass args as needed
            processed_tweets = []
            for tw in raw_tweets:
                processed_tweets.append(TWPreprocessor.preprocess_keyword(tw))
                    #indexer.create_documents(processed_tweets)

            indexer.create_documents(processed_tweets)
            keywords[i]["finished"] = 1
            keywords[i]["collected"] = len(processed_tweets)

            write_config({
                        "pois": pois, "keywords": keywords
                })

            save_file(processed_tweets, f"keywords_sep_{keywords[i]['id']}.pkl")

            print("------------ process complete -----------------------------------")

    if reply_collection_knob:
        # Write a driver logic for reply collection, use the tweets from the data files for which the replies are to collected.
        for i in range(len(pois)):
            print(pois[i]["reply_finished"])
            if pois[i]["reply_finished"] == 1:
                print(f"---------- collecting reply tweets for poi: {pois[i]['screen_name']}")
                screen_name = pois[i]['screen_name']
                type = pois[i]['lang']
                N = 100
                raw_tweets = twitter.get_tweets_by_poi_screen_name(screen_name, type, N)
                processed_reply = []
                for twt in raw_tweets:
                    replies = twitter.get_replies(twt, 10)

                    for rp in replies:
                        print(rp.full_text)
                        processed_reply .append(TWPreprocessor.preprocess_reply(rp))

                indexer.create_documents(processed_reply )

                pois[i]["reply_finished"] = 1
                pois[i]["collected_rp"] = len(processed_reply )

                write_config({
                        "pois": pois, "keywords": keywords
                })

                save_file(processed_reply , f"poi_rp_{pois[i]['id']}.pkl")
                print("------------reply process complete -----------------------------------")

        #raise NotImplementedError


if __name__ == "__main__":
    main()
