import re
import string
class gCodeParser(object):
    
    def __init__(self):
        self.gCodeLib={}
        let=['A','B','C','D']; 
        for letter in let:
            #filename='gCodeReader/' + letter + 'Gcode.Dnc';
            filename = letter + 'Gcode.Dnc'
            gcodeFile=open(filename);
            info=gcodeFile.read();
            self.gCodeLib[letter]=info;
    
    #Obtains the right GCode from the Gcode map
    def toGcode(self,parsedLetter):
        for key in self.gCodeLib.keys():
            if key==parsedLetter:
                strPrint = self.gCodeLib[key];
                strPrint = re.sub("N\w+", '', strPrint);
                strPrint = str(strPrint);
                strPrint = strPrint.lstrip()
                return strPrint;

    def stringToArrayParser(self,stringToParse):
        return list(stringToParse);
