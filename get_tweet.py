import oath, json, config

def tweet_search(search_word):
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
  params = {
    "q": search_word,
    "lang": "ja",
    "result_type": "recent",
    "count": "15"
  }
  session = oath.create_oath_session()
  response = session.get(url, params=params)
  if response.status_code != 200:
    print("Error code: %d" % (response.status_code))
    return None
  tweets = json.loads(response.text)
  #print(tweets)
  return tweets

def get_timeline():
  url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
  params = {
    "screen_name": config.SCREEN_NAME,
    "count": 100,
    "exclude_replies": "true",
    "include_rts": "false"
  }
  session = oath.create_oath_session()
  response = session.get(url, params=params)
  if response.status_code != 200:
    print("Error code: %d" % (response.status_code))
    return None
  tweets = json.loads(response.text)
  return tweets
