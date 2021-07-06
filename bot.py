import tweepy, time
print('Bot is here')
CONSUMER_KEY = "1OpaYPXLqymWZ8KmW6odnfHmL"
CONSUMER_SECRET = "qBaIRmOtF3hlLSr6UaE6zZGzEB2OIyLnTZ0pZTOJB5qGvnJII6"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAEyORQEAAAAA51%2Fa4z4%2BZfVMt4EGeSGk73LikHA%3DUPheSlkjnSFPG9Zo9p82nijY2s75Lha4zsM5hP8XtCI8RswieW"
ACCESS_KEY = "2945480147-arP2RiUYTryqoUQtzcxMUn1aX15Im2h0kYWnp4p"
ACCESS_SECRET = "7FOp554qn7W43hcauyNVl0ddSLPgPJDobhaI7WcNUC3Gd"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

def retreive_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

FILE_NAME_TEST = 'test_tweet.txt'

def test_tweet():
    print('Retreaving tweets...')
    last_seen_id = retreive_last_seen_id(FILE_NAME_TEST)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode = "extended")
    for mention in reversed(mentions):
        if not mention:
            return
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_test_tweet = mention.id
        store_last_seen_id(last_test_tweet,FILE_NAME_TEST)
        print('found @elizabot9', flush=True)
        print('fav-ing and retweeting tweet...', flush=True) 
        api.create_favorite(mention.id)
        api.retweet(mention.id)
while True:
    test_tweet()
    time.sleep(15)