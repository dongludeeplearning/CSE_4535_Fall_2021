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

        clean_text, emojis = _text_cleaner(tweet.full_text)


        poi_dict={"id": tweet.id,
             "poi_name": tweet.user.screen_name,
             "poi_id": tweet.user.id,
             "verified": tweet.user.verified,
             "tweet_text":tweet.full_text,
             "country": hard_country(tweet.lang),
             "tweet_lang": tweet.lang,
             "text_en": clean_text,
             "hashtags": _get_entities(tweet,'hashtags'),
             "mentions":_get_entities(tweet,'mentions'),
             "emoticons":emojis,
             "tweet_date":_get_tweet_date(str(tweet.created_at)).isoformat()
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
        clean_text, emojis= _text_cleaner(tweet.full_text)

        # for keyword tweet gen json
        keyword_dict = {"id": tweet.id,
                    "verified": tweet.user.verified,
                    "country": hard_country(tweet.lang),
                    "tweet_text": tweet.full_text,
                    "tweet_lang": tweet.lang,
                    "text_en": clean_text,
                    "hashtags": _get_entities(tweet, 'hashtags'),
                    "tweet_urls": _get_entities(tweet, 'urls'),
                    "tweet_date": _get_tweet_date(str(tweet.created_at)).isoformat(),
                    "geolocation": tweet.user.location
                    }

        return keyword_dict
        raise NotImplementedError

    @classmethod
    def preprocess_reply(cls, tweet):
        '''
        Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
        :param tweet:
        :return: dict
        '''
        clean_text, emojis = _text_cleaner(tweet.full_text)

        # for keyword tweet gen json
        reply_dict = {"id": tweet.id,
                    "verified": tweet.user.verified,
                    "country": hard_country(tweet.lang),
                    "replied_to_tweet_id": tweet.in_reply_to_status_id,
                    "replidd_to_user_id": tweet.in_reply_to_user_id,
                    "reply_text": clean_text,
                    "tweet_text": tweet.full_text,
                    "tweet_lang": tweet.lang,
                    "tween_en": clean_text,
                    "mentions": _get_entities(tweet, 'user_mentions'),
                    "tweet_date": _get_tweet_date(str(tweet.created_at)).isoformat(),
                    "geolocation": tweet.user.location
                        }

        return reply_dict
        raise NotImplementedError


# hard core country
def hard_country(lang):
    H_country=[]
    if lang == "en":
        H_country = "USA"
    if lang == "hi":
        H_country = "INDIA"
    if lang == "es":
        H_country = "MEXICO"
    return H_country


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
    #return clean_text
    return clean_text, emojis


# def _get_tweet_date(tweet_date):
#     tweet_date= tweet_date.strftime('%X-%m %d %H:%M:%S')
#     return tweet_date


def _get_tweet_date(tweet_date):
    return _hour_rounder(datetime.datetime.strptime(tweet_date, '%Y-%m-%d %H:%M:%S'))

def _hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + datetime.timedelta(hours=t.minute // 30))




# test_code
# twitter = Twitter()
# key="quarentena"
# poi = "JoeBiden"
# raw_tweets = twitter.get_tweets_by_poi_screen_name(poi,"en",2)
# keyword_search=twitter.get_tweets_by_lang_and_keyword(key,"en",5)
## reply_tweets= twitter.get_replies(tweet, n)
# for twt in raw_tweets:
#     #print(twt.full_text)
#     print(TWPreprocessor.preprocess_poi(twt))
# for tweet in keyword_search:
#     print(TWPreprocessor.preprocess_keyword(tweet))
