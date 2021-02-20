import tweepy
import json

consumer_key = "4C01PjIV6cXsmGw6p6N0SoRuE"
consumer_secret = "KNiyMxTrtzwxDRljlqNfJTZIOqAbCgTq1jdNvWk86BKvxVv2vY"
access_token = "917511810688999424-wuhA3qMtQ0aqywjcNKvbfc6IU4i65VD"
access_token_secret = "OuwBWadPlNFw5XbRfZFDGcIFygi6DzumtAkf4rEpFjmKx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# data = api.me() // Ver información de mi perfil
# data = api.get_user("freddier") // Ver información de un usuario

# Obtener Followers de un Usuario usando Cursor

# data = api.followers(screen_name="freddier")
# for user in tweepy.Cursor(api.followers, screen_name="freddier").items(10):
#    print (json.dumps(user._json, indent=2))

# Obtener un Timeline
for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extendend").items(1):
    print (json.dumps(tweet._json, indent=2))
