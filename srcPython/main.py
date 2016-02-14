from gCodeReader.toGcode import gCodeParser
from interfaces.arduinoInterface import ArduinoInterface
from repeatedFunction import RepeatedTimer
from TwitterAPIGet import twitterInteractor


parser = gCodeParser()
ardInterface = ArduinoInterface()
twitterAPI = twitterInteractor()


def checkTweet():
    print "finding twitter message";
    tweet = twitterAPI.getLatest()
    if tweet!=None:
        sendToPrint(tweet);
    else:
        print 'do nothing'
    
def sendToPrint(message):
    arrayMessage = parser.stringToArrayParser(message)
    for parsedCharacter in arrayMessage:
        gCodes = parser.toGcode(parsedCharacter);
        ardInterface.sendGCode(gCodes);

print 'connecting to arduino';
print 'changes are in effect';
ardInterface.connectToArd();        
#checkTweet()
repeatFn = RepeatedTimer(2.0,checkTweet);
