from arduinoInterface import *

ardInterface = ArduinoInterface();
print 'connecting to Ard';
ardInterface.connectToArd();
print 'connected yahoo'

ardInterface.sendGCode('G0 X100');

ardInterface.sendGCode('G0 X98');

ardInterface.sendGCode('G0 X1');

