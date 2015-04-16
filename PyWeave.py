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
        self.weftThreads = weftThreads
        self.tieUp = tieUp
        self.threading = threading
        self.treadling = treadling
        self.warpColors = warpColors
        self.weftColors = weftColors
    
    ## alternate constructor that loads .WIF file
    
    def __init__(self, fileName):
        try:
            # open file and check it's a .wif
            file = open(fileName, 'r')
            if file.readline().strip() != "[WIF]":
                raise

            # read through file
            header = "[WIF]"                # stores current section header
            for line in file.readlines():   # iterate through lines
                line = line.strip()         # strip away whitespace
                
                if line[0] == "[":          # check if line is a section header
                    header = line
                else:                       # otherwise process the line
                    # process color table lines (x=xxx,xxx,xxx)
                    if header == "[COLOR TABLE]":
                        line = line.split("=")
                        line[1] = line[1].split(",")
                        self.colorTable.append(line)
                        
                    # look for warp and weft threads
                    elif header == "[WEFT]":
                        line = line.split("=")
                        if line[0] == "Threads":
                            self.weftThreads = int(line[1])
                            
                    elif header == "[WARP]":
                        line = line.split("=")
                        if line[0] == "Threads":
                            self.warpThreads = int(line[1])
                            
                    # fill tieup table
                    elif header == "[TIEUP]":
                        line = line.split("=")
                        line[1] = line[1].split(",")
                        self.tieUp.append(line)
                        
                    # fill threading table
                    elif header == "[THREADING]":
                        self.threading.append(line.split("="))
                        
                    # fill treadling table
                    elif header == "[TREADLING]":
                        self.treadling.append(line.split("="))
                        
                    # fill in colors
                    elif header == "[WARP COLORS]":
                        self.warpColors.append(line.split("="))
                        
                    elif header == "[WEFT COLORS]":
                        self.weftColors.append(line.split("="))
                        
            file.close()
        except:
            print("Error loading .WIF file!")
        
    
    ## saves a bitmap image of the weave
    
    # fileName - filename to save as
    # scale - width of each thread in pixels (default 1)
    # spacing - amount of pixels to put in between each thread (default 0)
    
    def saveBitmap(self, fileName, scale = 1, spacing = 0):
        print(self)
        ###
        ## TODO
        ###

# akin to 'main' method, will only run if this specific file is run
if __name__ == "__main__":
    weave = Weave("test.wif")
    weave.saveBitmap("output.bmp")
    