import twitter

class twitterInteractor(object):
    #initializes the API
    def __init__(self):
        self.api = twitter.Api(consumer_key='yoiO2TaQieEEPqYnxc1Z2psMa',
                              consumer_secret='z7iZvzznu4mOZdtW0Tmkcuzf2BSpNbzixnaZ9qeTrNVInCfFoh',
                              access_token_key='3248255634-prUKd6kdkXGBMmZxmDcya1LEEZ6zKKLPCA79eqV',
                              access_token_secret='O31W2rtfAnc3KWdakedNJcEOzoomzVuoiufVZqAdJQGQQ')
        self.currentTweet = ""
    
    #gets the latest tweet and returns it to the user
    def getLatest(self):
        statusTweets = self.api.GetUserTimeline(screen_name='nesh170',count=1)
        if self.currentTweet != statusTweets[0]:
            self.currentTweet = statusTweets[0]
            output = statusTweets[0].text
        else:
            output = None;
        return output