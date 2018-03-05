import tweepy
from textblob import TextBlob
import csv

consumer_key =''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

search_param = 'Tesla'

csv_file = open('twitter_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Keyword', 'Tweet', 'Polarity -1/1', 'Subjectivity 0/1'])

api = tweepy.API(auth)

public_tweet = api.search(search_param)

for tweet in public_tweet:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    csv_writer.writerow([search_param, tweet.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity])
    print()

csv_file.close()
# polarity = how positive/negative the tweet it
# subjectivity = opinion or factual