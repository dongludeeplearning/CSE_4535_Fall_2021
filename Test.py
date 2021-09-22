import tweepy
import pickle
import json
#
# auth = tweepy.OAuthHandler("ISkrSjEx0ML1H35UYdVZAXfS3", "z5wAiKfIlMzvabBf99eHVoM2qSEl9x2m46ypwZU6xKy7BYI8FD")
# auth.set_access_token("1432528446312304640-DRGnfgujqMNajxlWTQ7CHCdhiMvOSU", "dHBGfKReNC95oUyiOCZueDyGOJDidSHXX0pSYmb5JwCPa")
# api = tweepy.API(auth)
#
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# user = api.get_user('JoeBiden')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)


# with open('project1/data/poi_1.pkl', 'rb') as f:
#     c = pickle.load(f)
# print(c)

with open('project1/config.json', 'r') as outfile:
    config= json.load(outfile)
print(config)