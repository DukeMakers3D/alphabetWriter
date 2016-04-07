import requests
from time import sleep
from arduinoInterface import *

ardInterface = ArduinoInterface();
print 'connecting to Ard';
ardInterface.connectToArd();
print 'connected yahoo'
printed_before = False;
gcode_list = [' G0 X100', ' G0 X98', ' G0 X1'];

def send_the_print(state_bool):
    if(state_bool):
        print 'State: ' + str(state_bool);
    else:
        for txt in gcode_list:
            ardInterface.sendGCode(txt);
            print txt;
    sleep(2)    
    return True;

while(True):
    r = requests.get('http://colab-sbx-56.oit.duke.edu/switchStateID/1')
    state_of_switch = r.json()['state']
    if((state_of_switch=='ON')):
        printed_before = send_the_print(printed_before);
    else:
        printed_before = False;
        sleep(2);   