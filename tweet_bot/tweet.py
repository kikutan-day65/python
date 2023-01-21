import tweepy
import time

auth = tweepy.OAuthHandler("API key", "API key secret")
auth.set_access_token("Access token", "Access token secret")

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_str = "cleveland guardians"
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_str).items(numbersOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# generous bot
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
    if follower.name == 'dobryden':
        follower.follow()
        break