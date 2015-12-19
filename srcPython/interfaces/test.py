from arduinoInterface import *

ardInterface = ArduinoInterface();

ardInterface.connectToArd();

ardInterface.sendGCode('G0 X0');

ardInterface.sendGCode('G0 X50');

ardInterface.sendGCode('G0 X0');

ardInterface.sendGCode('G0 X100');

