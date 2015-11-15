from gCodeReader.toGcode import *
from interfaces.arduinoInterface import *
from repeatedFunction import RepeatedTimer
from TwitterAPIGet import twitterInteractor


parser = gCodeParser()
ardInterface = ArduinoInterface()
twitterAPI = twitterInteractor()


def checkTweet():
    tweet = twitterAPI.getLatest()
    if tweet!=None:
	print tweet;
        sendToPrint(tweet);
    
def sendToPrint(message):
     arrayMessage = parser.stringToArrayParser(message)
     for parsedCharacter in arrayMessage:
         gCodes = parser.toGcode(parsedCharacter);
	 print gCodes;
         ardInterface.sendGCode(gCodes);

print 'connecting to arduino';
ardInterface.connectToArd();        
repeatFn = RepeatedTimer(2.0,checkTweet);


