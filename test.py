import tweepy
from os import getenv
import urllib3
urllib3.disable_warnings()

auth = tweepy.OAuthHandler(
    getenv('CONSUMER_PUBLIC_KEY'),
    getenv('CONSUMER_PRIVATE_KEY'))

auth.set_access_token(
    getenv('ACCESS_TOKEN'),
    getenv('ACCESS_TOKEN_SECRET')
)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()

user = api.get_user('realDonaldTrump')
print(user.id)
print(dir(user))
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name

trumpkins = set(api.followers_ids('realDonaldTrump'))
clintons = set(api.followers_ids('HillaryClinton'))

both = trumpkins.intersection(clintons)
for x in list(both)[0:5]:
    print(api.get_user(x).screen_name)

# print("\n\n\n\n")
# rts = api.retweets(760783130978648064)


# for tweet in public_tweets:
#     print(dir(tweet))
#     if tweet.location:
#         print(tweet)
