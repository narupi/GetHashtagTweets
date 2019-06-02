import get_tweet, config, re

def date_molding(date):
  day_of_the_week, month, day, time, _, year = date.split()
  molded = year + " " + month + "/" + day + "(" + day_of_the_week + ") " + time
  return molded
    
def check_duplicate(tweet_id):
  file_activity_id = "./activity_id.txt"
  try:
    read = open(file_activity_id, 'r')
    lines = read.readlines()
    for line in lines:
      if tweet_id in line:
        read.close()
        return False
    
  except Exception as e:
    print(e)

  finally:
    read.close()
    
  return True
  

def postscript(tweet):
  file_activity = "./activity.txt"
  file_activity_id = "./activity_id.txt"
  write_data = (re.sub(r'(?m)^#.*',"",tweet['text']).rstrip('\n') + '\n' + date_molding(tweet['created_at'])+'\n\n')
  
  if check_duplicate(tweet['id_str']):
    try:
      write = open(file_activity, 'a')
      write.write(write_data)
    except Exception as e:
      print(e)
    finally:
      write.close()
      
    try:
      write_id = open(file_activity_id, 'a')
      write_id.write(tweet['id_str']+'\n')
    except Exception as e:
      print(e)
    finally:
      write_id.close()

  return 

def main():
  tweets = get_tweet.get_timeline()
  for tweet in tweets:
      hashtags = [lst.get('text') for lst in tweet['entities']['hashtags']]
      if config.KEYWORD_HASHTAG in hashtags:
        postscript(tweet)
      

if __name__ == "__main__":
  main()
