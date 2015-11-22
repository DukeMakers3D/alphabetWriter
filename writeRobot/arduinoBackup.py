import pexpect

class ArduinoInterface():

    def __init__(self):
        self.child = pexpect.spawn('Printrun/pronsole.py');
        
    def connectToArd(self):
        self.child.expect('offline>');
        print self.child.before;
        self.child.sendline('connect /dev/ttyACM0 250000');
        self.child.expect('PC>');
        print self.child.before;
        self.child.sendline('G0 X200');
        print self.child.after;


        
        self.child.expect_exact('PC>');
        print self.child.before;
        self.child.sendline('G0 X0');
        print self.child.after;

    def sendGCode(self,gcodeString):
        self.child.sendline('G0');
        self.child.expect('98>');
        print self.child.before;
        self.child.sendline(gcodeString);







