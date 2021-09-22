'''
@author: Souvik Das
Institute: University at Buffalo
'''

import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler("ISkrSjEx0ML1H35UYdVZAXfS3", "z5wAiKfIlMzvabBf99eHVoM2qSEl9x2m46ypwZU6xKy7BYI8FD")
        self.auth.set_access_token("1432528446312304640-DRGnfgujqMNajxlWTQ7CHCdhiMvOSU", "dHBGfKReNC95oUyiOCZueDyGOJDidSHXX0pSYmb5JwCPa")
        self.api = tweepy.API(self.auth)

       
    def _meet_basic_tweet_requirements(self,tweetcollection, testnumber):
        '''
        Add basic tweet requirements logic, like language, country, covid type etc.
        :return: boolean
        '''
        # pass in tweet and judge
        # test language 5k for en, hi, es
        if testnumber==0:
            en_sum=0
            hi_sum=0
            es_sum=0
            for twt in tweetcollection:
                if twt.lang=="en":
                    en_sum+=1
                if twt.lang=="hi":
                    hi_sum+=1
                if twt.lang=="es":
                    es_sum+=1
            print("en_langugae:",en_sum, "hi_language:",hi_sum,"es_language:", es_sum)

        # elif testnumber==1:   # test country
        #     USA=0
        #     INDIA=0
        #     MEXICO=0
        #     for twt in tweetcollection:
        #         if twt.country=="USA":
        #             USA+=1
        #         if twt.country=="INDIA":
        #             INDIA+=1
        #         if twt.country == "MEXICO":
        #             MEXICO+=1
        #     print("USA:", USA, "INDIA:", INDIA, "MEXICO:", MEXICO)
        #
        # else # test covid type
        #      return true
        # elif testnumber==1:
        #      test country
        #      return true
        # else testnumber==2:
        #      test covid type
        #      return true

        raise NotImplementedError

    def get_tweets_by_poi_screen_name(self,screen_name):
        '''
        Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
        :return: List
        '''
        poi_search = tweepy.Cursor(self.api.user_timeline, id=screen_name, lang='en', verified='true',
                                        tweet_mode='extended').items(500)
        return poi_search
        raise NotImplementedError

    def get_tweets_by_lang_and_keyword(self, keywords):
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        :return: List
        '''
        keyword_search = tweepy.Cursor(self.api.search, q=keywords, lang='en',tweet_mode='extended').items(500)
        return keyword_search
        raise NotImplementedError

    def get_replies(self, tweet):
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''
        tweet_id = tweet.id
        user_name = tweet.user.screen_name
        max_id = None
        replies = tweepy.Cursor(self.api.search, q='to:' + user_name, since_id=tweet_id, max_id=max_id, result_type='recent', tweet_mode='extended').items(10)
        return replies
        raise NotImplementedError


# # #test code
# twitter = Twitter()
# # poi="JoeBiden"
# key="#covid vaccine"
# # raw_tweets = twitter.get_tweets_by_poi_screen_name(poi)
# keyword_search=twitter.get_tweets_by_lang_and_keyword(key)
# for i in keyword_search:
#     print(i.full_text)
# #      replies=twitter.get_replies(i)
# #      print (replies)