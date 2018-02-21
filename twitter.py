import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():

# Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "tZjbw3pQHq7RSoWIydmdsMGF7",
    "consumer_secret"     : "6Wk5bckQdzHjBrMiS9zP45WIuyASu3GWRr8uwt0BIyTN6kIpeb",
    "access_token"        : "3229002192-pzwnGBOin2cpBI0AAusLEyzkVURqd6O78NeMGMz",
    "access_token_secret" : "ufBdxnSXfnWyJyEdDk9ljQ3ZtS7xGT1bR2VOfn7iQr4Lx" 
    }

  api = get_api(cfg)
  tweet = "HI computer"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
