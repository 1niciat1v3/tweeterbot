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