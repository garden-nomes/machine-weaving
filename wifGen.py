# Relably creates random weaves that can be processed directly by machine-weaving pyweave
# KNOWN ISSUES:
#   -Only has one tieup pattern hard-wired in, so the range of design is limited
#   -Only outputs wif to terminal and does not save it to file


# need random values for colors and number of warps and wefts
import random


# lots of print statements that print out the headers and whatnot
# then there is some filler lines that produce the actual information

def wifGen():
    print('[WIF]')
    print('[COLOR TABLE]')

    # assign color1 three random ints between 0 and 255
    color1 = str((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    print('1='+color1.strip('()').replace(' ',''))

    # assign color2 three random ints for its color
    color2 = str((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    print('2='+color2.strip('()').replace(' ',''))

    print('[WARP]')
    # give a random amount of warp threads
    threads1 = random.randint(1,100)
    print('Threads='+str(threads1))

    print('[WEFT]')
    # give random amount of weft threads
    threads2 = random.randint(1,100)
    # always make sure that there are more weft threads than warp threads
    while threads2 < threads1:
        threads2 = random.randint(1,100)
    print('Threads='+str(threads2))



    # this section is 'hard-wired' in currently,
    # but would like to be able to have this changed randomly or upon input at some point
    print('[TIEUP]')
    print('1=1,2')
    print('2=2,3')
    print('3=1,4')
    print('4=2,3')

    # assign each thread in the warp to a tieup number
    print('[THREADING]')
    for x in range(threads1):
        print(str(x)+'='+str(random.randint(1,4)))

    # assign each thread in the weft to a tieup number
    print('[TREADLING]')
    for x in range(threads2):
        print(str(x)+'='+str(random.randint(1,4)))

    # assign warp threads to color1
    print('[WARP COLORS]')
    for x in range(threads1):
        print(str(x)+'='+'1')

    # assign weft threads to color 2
    print('[WEFT COLORS]')
    for x in range(threads2):
        print(str(x)+'='+'2')

#run the script
wifGen()
