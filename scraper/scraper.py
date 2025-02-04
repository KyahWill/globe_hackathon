import tweepy
import requests

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Verify the authentication
try:
    api.verify_credentials()
    print("Authentication successful!")
except Exception as e:
    print("Error during authentication:", e)
    


# Define the endpoint and query parameters
endpoint = "https://api.twitter.com/2/tweets/search/recent"
query = "globe mabagal"  # Replace with your query or hashtag
max_results = 10  # Limit the results to fit free tier (max 100)

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

params = {
    "query": query,
    "max_results": max_results  # Max is 100 for free-tier
}

# Make the request
response = requests.get(endpoint, headers=headers, params=params)

if response.status_code == 200:
    tweets = response.json()
    for tweet in tweets['data']:
        print(f"Tweet: {tweet['text']}")
else:
    print(f"Error: {response.status_code}")
