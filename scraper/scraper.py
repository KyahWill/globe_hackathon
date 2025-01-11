import tweepy
import requests
import csv
import os
import json
import time
#from dotenv import load_dotenv

# Load the .env file
#load_dotenv()

# consumer_key = os.getenv('API_KEY')
# consumer_secret = os.getenv('API_KEY_SECRET')
# BEARER_TOKEN = os.getenv('BEARER_TOKEN')
# access_token = os.getenv('ACCESS_TOKEN')
# access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

consumer_key = 'lhucYjntKF5MILuCwGz6LAjCi'
consumer_secret = 'DK6M0Ky3wE6iCzHel6x2v0wF5OmmbL5Fxbl3kjM3JLXw57mG9Y'
access_token = '3671522653-MAJzCMi1pdNqzVVoRC1BC1y8c9TX2GiQqaQDC0K'
access_token_secret = 'LtQBO1zZvcKfLLDJPmyE37pYhArIEPhNQPPTTcKCQFl0i'
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGBLyAEAAAAAgbHPtj0tx6mCdgUMl9cGyhJ%2Bebg%3DX8MhlNmiMQtNM0w5DuVbi4qtzCBaI2f16JddU5UHca6s0qxPt6"

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
query = "@enjoyGLOBE"  # Replace with your query or hashtag
max_results = 10  # Limit the results to fit free tier (max 100)

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

params = {
    "query": query,
    "max_results": max_results  # Max is 100 for free-tier
}

# Path to the input CSV file
csv_file_path = 'testData1.csv'  # Replace with the actual file path

# Read CSV data
csv_data = []
# with open(csv_file_path, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         csv_data.append(row)

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        processed_row = {
            "author": row.get("Author", ""),
            "date_created": row.get("Created_At", ""),
            "id": row.get("Post_ID", ""),
            "text": row.get("Post_Text", ""),
            "platform": row.get("Platform", ""), 
        }
        csv_data.append(processed_row)
        
json_file_path = 'fromCsv.json'

# Open a JSON file to write the data
with open(json_file_path, 'w', encoding='utf-8') as file:
    # Save the data directly in JSON format
    json.dump(csv_data, file, indent=4)

print(f"Tweets have been saved to {json_file_path}")
        
def fetch_tweets():
    # Make the request
    response = requests.get(endpoint, headers=headers, params=params)

    # Path to save JSON file
    json_file_path2 = 'fromScraped.json'
 
    # Scraped data to JSON
    if response.status_code == 200:
        tweets = response.json()
        processed_tweets = []

        # Process each tweet to include the required fields
        if 'data' in tweets:
            for tweet in tweets['data']:
                processed_tweet = {
                    "author": "",  # Empty author field
                    "date_created": "",  # Empty date_created field
                    "id": tweet.get("id", ""),
                    "text": tweet.get("text", ""),
                    "platform": "Twitter"  # Static platform field
                }
                processed_tweets.append(processed_tweet)

        # Save processed data to JSON
        with open(json_file_path2, 'w', encoding='utf-8') as file:
            json.dump(processed_tweets, file, indent=4)

        print(f"Tweets have been saved to {json_file_path2}")
    else:
        print(f"Error: {response.status_code}")
    
# Run the request every 5 minutes (300 seconds)
while True:
    fetch_tweets()
    print("Waiting for the next request...")
    time.sleep(300)  # Sleep for 5 minutes