from gCodeReader.toGcode import *
from interfaces.arduinoInterfaces import *
from repeatedFunction import RepeatedTimer
from TwitterAPIGet import twitterInteractor


parser = gCodeParser()
ardInterface = ArduinoInterface()
twitterAPI = twitterInteractor()


def checkTweet():
    tweet = twitterAPI.getLatest()
    if tweet!=None:
        sendToPrint(tweet);
    
def sendToPrint(message):
     arrayMessage = parser.stringToArrayParser(message)
     for parsedCharacter in arrayMessage:
         gCodes = parser.toGcode(parsedCharacter)
         ardInterface.sendGCode(gCodes);


ardInterface.connectToArd()        
repeatFn = RepeatedTimer(2.0,checkTweet)


