from PIL import Image
import wifGen

class Weave:

    ## data structures

    colorTable = {}   # for now we'll only deal with RGB values from 0 to 255,
                      # although .WIF supports other formats
    warpThreads = 0   # let's not worry about units and spacing and whatnot yet
    weftThreads = 0
    tieUp = {}        # this would represent the top-right quandrant in WeavePoint
    threading = []    # this is the top-left quandrant
    treadling = []    # and this the bottom-right quadrant
    warpColors = []   # corresponds with the color table
    weftColors = []

    ## basic constructor that takes weave as arguments

    def __init__(self, colorTable, warpThreads, weftThreads, tieUp,
                 threading, treadling, warpColors, weftColors):
        self.colorTable = colorTable
        self.warpThreads = warpThreads
        self.weftThreads = weftThreads
        self.tieUp = tieUp
        self.threading = threading
        self.treadling = treadling
        self.warpColors = warpColors
        self.weftColors = weftColors

    ## alternate method that loads .WIF file
    
    @classmethod
    def loadWIF(cls, fileName):
        colorTable = {}   # for now we'll only deal with RGB values from 0 to 255,
                          # although .WIF supports other formats
        warpThreads = 0   # let's not worry about units and spacing and whatnot yet
        weftThreads = 0
        tieUp = {}        # this would represent the top-right quandrant in WeavePoint
        threading = []    # this is the top-left quandrant
        treadling = []    # and this the bottom-right quadrant
        warpColors = []   # corresponds with the color table
        weftColors = []
        
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

                # process color table lines (x=xxx,xxx,xxx)
                elif header == "[COLOR TABLE]":
                    line = line.split("=")
                    index = int(line[0])                    # convert index to int
                    # convert every item in the color array to int
                    color = [int(x) for x in line[1].split(",")]

                    colorTable[index] = color

                # look for warp and weft threads
                elif header == "[WEFT]":
                    line = line.split("=")
                    if line[0] == "Threads":
                        weftThreads = int(line[1])

                elif header == "[WARP]":
                    line = line.split("=")
                    if line[0] == "Threads":
                        warpThreads = int(line[1])

                # fill tieup table
                elif header == "[TIEUP]":
                    line = line.split("=")
                    index = int(line[0])
                    # convert each item to int
                    harnesses = [int(x) for x in line[1].split(",")]
                    tieUp[index] = harnesses

                # fill threading table
                elif header == "[THREADING]":
                    threading.append(int(line.split("=")[1]))

                # fill treadling table
                elif header == "[TREADLING]":
                    treadling.append(int(line.split("=")[1]))

                # fill in colors
                elif header == "[WARP COLORS]":
                    warpColors.append(int(line.split("=")[1]))

                elif header == "[WEFT COLORS]":
                    weftColors.append(int(line.split("=")[1]))

            file.close()
        except:
            print("Error loading .WIF file!")
        
        return cls(colorTable, warpThreads, weftThreads, tieUp,
                   threading, treadling, weftColors, warpColors)


    ## saves a bitmap image of the weave

    # fileName - filename to save as
    # scale - width of each thread in pixels (default 1)
    # spacing - amount of pixels to put in between each thread (default 0)

    def saveBitmap(self, fileName, scale = 1, spacing = 0):
        # step 1: generate image as string
        # step 2: create image using PIL's fromstring method

        # initialize string buffer

        imgString = ""

        # iterate over rows and pixels

        for i in range(0, self.weftThreads * scale):
            for j in range(0, self.warpThreads * scale):
                weftThread = int(i / scale)
                warpThread = int(j / scale)

                # decide if warp thread or weft thread is showing

                if self.threading[warpThread] in self.tieUp[self.treadling[weftThread]]:
                    color = self.colorTable[self.warpColors[warpThread]]
                else:
                    color = self.colorTable[self.weftColors[weftThread]]

                imgString += chr(color[0]) + chr(color[1]) + chr(color[2])

        # create image from buffer

        image = Image.frombytes(
            "RGB", (self.warpThreads * scale, self.weftThreads * scale), imgString)

        # save image

        image.save(fileName)
        image.show()
    
    def saveWIF(self, filename):
        try:
            file = open(filename, 'w')

            file.write('[WIF]''\n')
            file.write('[COLOR TABLE]''\n')

            # assign color1 three random ints between 0 and 255
            file.write('1='+str(probWeave.pickColor().strip('()').replace(' ',''))+'\n')

            # assign color2 three random ints for its color
            file.write('2='+str(probWeave.pickColor().strip('()').replace(' ',''))+'\n')

            file.write('[WARP]''\n')
            # give a random amount of warp threads
            threads1 = random.randint(1,255)
            file.write('Threads='+str(threads1)+'\n')

            file.write('[WEFT]''\n')
            # give random amount of weft threads
            threads2 = random.randint(1,255)
            while threads2 < threads1:
                threads2 = random.randint(1,255)
            file.write('Threads='+str(threads2)+'\n')


            file.write('[TIEUP]''\n')
            harness1 = (random.randint(1,2),random.randint(1,2))
            file.write('1='+str(harness1).strip('()').replace(' ','')+'\n')
            harness2 = (random.randint(2,3),random.randint(2,3))
            file.write('2='+str(harness2).strip('()').replace(' ','')+'\n')
            harness3 = (random.randint(3,4),random.randint(3,4))
            file.write('3='+str(harness3).strip('()').replace(' ','')+'\n')
            harness4 = (random.randint(1,4),random.randint(1,4))
            file.write('4='+str(harness4).strip('()').replace(' ','')+'\n')

            # assign each thread in the warp to a tieup number
            file.write('[THREADING]''\n')
            for x in range(0, threads1, 2):
                file.write(str(x)+'='+str(random.randint(1,3))+'\n')
            for x in range(1, threads1, 2):
                file.write(str(x)+'='+str(random.randint(2,4))+'\n')

            # assign each thread in the weft to a tieup number
            file.write('[TREADLING]''\n')
            for x in range(0, threads2, 2):
                file.write(str(x)+'='+str(random.randint(1,3))+'\n')
            for x in range(1, threads2, 2):
                file.write(str(x)+'='+str(random.randint(2,4))+'\n')

            # assign warp threads to color1
            file.write('[WARP COLORS]''\n')
            for x in range(threads1):
                file.write(str(x)+'='+'1'+'\n')

            # assign weft threads to color 2
            file.write('[WEFT COLORS]''\n')
            for x in range(threads2):
                file.write(str(x)+'='+'2'+'\n')

            file.close()

# akin to 'main' method, will only run if this specific file is run
if __name__ == "__main__":
    wifGen.wifGen()
    weave = Weave.loadWIF("testWIF.wif")
    weave.saveBitmap("output.bmp", 10)
    
