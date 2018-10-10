""" we can print the previous code in form of a JSON
The JSON response from the Twitter API is available in the attribute _json (with a leading underscore)
which is not the raw JSON string, but a dictionary."""

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
  process_or_store(status._json)

""" if we want to have a list of all our followers """
for friend in tweepy.Cursor(api.friends).items():
  process_or_store(friend._json)
  
""" if we want a list of all our tweets """ 
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    
    
""" In this way we can easily collect tweets (and more) and store them in the original JSON format, 
fairly easy to convert into different data models depending on our storage """
