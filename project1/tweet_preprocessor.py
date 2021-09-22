'''
@author: Souvik Das
Institute: University at Buffalo
'''




import datetime
import demoji
from twitter import Twitter
import preprocessor
import json
import datetime

class TWPreprocessor:
    @classmethod
    def preprocess_poi(cls, tweet):
        '''
        Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
        :param tweet:
        :return: dict
        '''
        # get country
        with open("config.json") as json_file:
            config=json.load(json_file)
        pois = config["pois"]
        keywords = config["keywords"]
        for i in range(len(pois)):
            if pois[i]["screen_name"] == tweet.user.screen_name:
                poicountry =pois[i]["country"]
        #
        # for i in range(len(keywords)):
        #     if keywords[i]['name'] == tweet.user.screen_name:
        #         keywords_country =keywords[i]["country"]

        # clean text
        #for poi tweet gen json
        poi_dict={"id": tweet.id,
             "poi_name": tweet.user.screen_name,
             "poi_id": tweet.user.id,
             "verified": tweet.user.verified,
             "tweet_text":tweet.full_text,
             "country": poicountry,
             "tweet_lang": tweet.lang,
             "text_en": _text_cleaner(tweet.full_text),
             "hashtags": _get_entities(tweet,'hashtags'),
             "mentions":_get_entities(tweet,'mentions'),
             "tweet_date":_get_tweet_date(tweet.created_at)
        }

        return poi_dict
        raise NotImplementedError

    @classmethod
    def preprocess_keyword(cls, tweet):
        '''
        Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
        :param tweet:
        :return: dict
        '''
        # get country
        if tweet.lang == "en":
            k_country = "USA"
        if tweet.lang == "hi":
            k_country = "INDIA"
        if tweet.lang == "es":
            k_country = "MEXICO"

        # for keyword tweet gen json
        keyword_dict = {"id": tweet.id,
                    "verified": tweet.user.verified,
                    "country": k_country,
                    "tweet_text": tweet.full_text,
                    "tweet_lang": tweet.lang,
                    "text_en": _text_cleaner(tweet.full_text),
                    "hashtags": _get_entities(tweet, 'hashtags'),
                    "tweet_date": _get_tweet_date(tweet.created_at)
                    }

        return keyword_dict

        raise NotImplementedError


# this function has been modified
def _get_entities(tweet, type=None):
    result = []
    if type == 'hashtags':
        hashtags = tweet.entities['hashtags']

        for hashtag in hashtags:
            result.append(hashtag['text'])
    elif type == 'mentions':
        mentions = tweet.entities['user_mentions']

        for mention in mentions:
            result.append(mention['screen_name'])
    elif type == 'urls':
        urls = tweet.entities['urls']

        for url in urls:
            result.append(url['url'])

    return result


def _text_cleaner(text):
    emoticons_happy = list([
        ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
        '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
        'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
        '<3'
    ])
    emoticons_sad = list([
        ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
        ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
        ':c', ':{', '>:\\', ';('
    ])
    all_emoticons = emoticons_happy + emoticons_sad

    emojis = list(demoji.findall(text).keys())
    clean_text = demoji.replace(text, '')

    for emo in all_emoticons:
        if (emo in clean_text):
            clean_text = clean_text.replace(emo, '')
            emojis.append(emo)

    clean_text = preprocessor.clean(text)
    # preprocessor.set_options(preprocessor.OPT.EMOJI, preprocessor.OPT.SMILEY)
    # emojis= preprocessor.parse(text)
    return clean_text
    #return clean_text, emojis


def _get_tweet_date(tweet_date):
    tweet_date=tweet_date.strftime('%a %b %d %H:%M:%S +0000 %Y')
    return tweet_date

def _hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + datetime.timedelta(hours=t.minute // 30))


# test_code

# twitter = Twitter()
# poi = "JoeBiden"
# #key="#quarentena"
# raw_tweets = twitter.get_tweets_by_poi_screen_name(poi)
# #keyword_search=twitter.get_tweets_by_lang_and_keyword(key)
# for tweet in raw_tweets:
#     print(TWPreprocessor.preprocess(tweet))


