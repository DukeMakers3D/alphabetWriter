def toGcode(aletter):
# Map/dictionary
    gcodelib={};
    let=['A','B','C','D']; # add in other letters later
    for letter in let:
        filename=letter+'Gcode.Dnc';
        file=open(filename);
        info=file.read();
        gcodelib[letter]=info;

    for key in gcodelib.keys():
        if key==aletter:
            print gcodelib[key];

# test function
print toGcode('B')


#print file.read()