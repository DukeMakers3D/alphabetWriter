from gCodeReader.toGcode import *
from interfaces.arduinoInterfaces import *

parser = gCodeParser()
lol = parser.stringToArrayParser('ABCD')
print lol

for k in lol:
    print parser.toGcode(k)