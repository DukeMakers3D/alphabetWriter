import pexpect

class ArduinoInterface(object):

    def __init__(self):
        self.child = pexpect.spawn('Printrun/pronsole.py');
        
    def connectToArd(self):
        self.child.expect('offline>');
        self.child.sendline('connect /dev/ttyACM0 250000');
        
    def sendGCode(self,gcodeString):
        self.child.expect('PC>');
        self.child.sendline(gcodeString);




