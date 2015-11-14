# Map/dictionary
gcodelib={};
let=['A','B','C','D'];
for letter in let:
    filename=letter+'Gcode.Dnc';
    file=open(filename);
    info=file.read();
    gcodelib[letter]=info;

print gcodelib
#Read file
#file = open('AGcode.Dnc', 'r')

#print file.read()