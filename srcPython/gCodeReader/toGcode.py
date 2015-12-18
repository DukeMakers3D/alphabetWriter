class gCodeParser(object):
    
    def __init__(self):
        self.gCodeLib={}
        let=['A','B','C','D']; 
        for letter in let:
            filename=letter+'Gcode.Dnc';
            gcodeFile=open(filename);
            info=gcodeFile.read();
            self.gCodeLib[letter]=info;
    
    #Obtains the right GCode from the Gcode map
    def toGcode(self,parsedLetter):
        for key in self.gCodeLib.keys():
            if key==parsedLetter:
                print self.gCodeLib[key];

    def stringToArrayParser(self,stringToParse):
        return list(stringToParse);