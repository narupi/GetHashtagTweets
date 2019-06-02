import config
from requests_oauthlib import OAuth1Session

def create_oath_session():
  CK = config.CONSUMER_KEY
  CS = config.CONSUMER_SECRET
  AT = config.ACCESS_TOKEN
  ATS = config.ACCESS_TOKEN_SECRET
  oath = OAuth1Session(CK, CS, AT, ATS)
  return oath
