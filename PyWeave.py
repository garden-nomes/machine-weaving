class Weave:
    
    ## data structures
    
    colorTable = []   # for now we'll only deal with RGB values from 0 to 255,
                      # although .WIF supports other formats
    warpThreads = 0   # let's not worry about units and spacing and whatnot yet
    weftThreads = 0
    tieUp = []        # this would represent the top-right quandrant in WeavePoint
    threading = []    # this is the top-left quandrant
    treadling = []    # and this the bottom-right quadrant
    warpColors = []   # corresponds with the color table
    weftColors = []
    
    ## basic constructor that takes weave as arguments
    
    def __init__(
            self, colorTable, warpThreads, weftThreads, tieUp,
            threading, treadling, warpColors, weftColors):
        self.colorTable = colorTable
        self.warpThreads = warpThreads
        self.tieUp = tieUp
        self.threading = threading
        self.treadling = treadling
        self.warpColors = warpColors
        self.weftColors = weftColors
    
    ## alternate constructor that loads .WIF file
    
    def __init__(self, fileName):
        #try:
            # open file and check it's a .wif
            file = open(fileName, 'r')
            
            if file.readline().strip() != "[WIF]":
                raise

            # read through lines
            lines = file.readlines()
            for i in range(0, len(lines)):
                
                # if line is the beginning of the color table
                if lines[i].strip() == "[COLOR TABLE]":
                    # fill color table
                    self.colorTable = []
                    for i in range(0, 10):
                        self.colorTable.append("")
                        
                    # loop until we reach a '['
                    j = i + 1
                    while lines[j][0] != "[":
                        # process line
                        line = lines[j].strip().split("=")
                        index = int(line[0])
                        print(index)
                        self.colorTable[index] = line[1].split(",")
                        # read next line
                        j += 1
                        
                    print(self.colorTable)
                        
            
            file.close()
        #except:
        #    print("Error loading .WIF file!")
        
    
    ## saves a bitmap image of the weave
    
    # fileName - filename to save as
    # scale - width of each thread in pixels (default 1)
    # spacing - amount of pixels to put in between each thread (default 0)
    
    def saveBitmap(self, fileName, scale = 1, spacing = 0):
        print("Eventually this will save a bitmap!")
        ###
        ## TODO
        ###

# akin to 'main' method, will only run if this specific file is run
if __name__ == "__main__":
    weave = Weave("test.wif")
    weave.saveBitmap("output.bmp")
    