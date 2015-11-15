import twitter

Tweet = ""
api = twitter.Api(consumer_key='yoiO2TaQieEEPqYnxc1Z2psMa',
                      consumer_secret='z7iZvzznu4mOZdtW0Tmkcuzf2BSpNbzixnaZ9qeTrNVInCfFoh',
                      access_token_key='3248255634-prUKd6kdkXGBMmZxmDcya1LEEZ6zKKLPCA79eqV',
                      access_token_secret='O31W2rtfAnc3KWdakedNJcEOzoomzVuoiufVZqAdJQGQQ')
def getLatest():
    global Tweet
    global api 
#     print api.VerifyCredentials()
    statusTweets = api.GetUserTimeline(screen_name='nesh170',count=1)
    if Tweet != statusTweets[0]:
        Tweet = statusTweets[0]
        output = statusTweets[0].text
    else:
        output = ""
    return output

print getLatest()
print getLatest()
print getLatest()
api.PostUpdate("yes")
print getLatest()
print getLatest()
api.PostUpdate("yes")
print getLatest()
print getLatest()