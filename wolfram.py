import random
from PyWeave import Weave

## generate first (seed) row of a wolfram cellular automata

def seed(width, probability = 0.5):
    pattern = []
    pattern.append([])
    
    for x in range(width):
        if random.random() < probability:
            pattern[0].append(True)
        else:
            pattern[0].append(False)
    
    return pattern

## append a single row to the pattern using a set of rules

def generate(pattern, rules):
    if len(rules) < 8:
        print("Invalid ruleset")
        return pattern
    
    row = len(pattern) - 1
    generation = []
    
    l = False if random.random() < 0.5 else True
    for x in range(len(pattern[row])):
        c = pattern[row][x]
        if x != len(pattern[row]) - 1:
            r = pattern[row][x + 1]
        else:
            r = False if random.random() < 0.5 else True
        
        if l and c and r:
            generation.append(rules[0])
        elif l and c and not r:
            generation.append(rules[1])
        elif l and not c and r:
            generation.append(rules[2])
        elif l and not c and not r:
            generation.append(rules[3])
        elif not l and c and r:
            generation.append(rules[4])
        elif not l and c and not r:
            generation.append(rules[5])
        elif not l and not c and r:
            generation.append(rules[6])
        elif not l and not c and not r:
            generation.append(rules[7])
        
        l = c
    
    return generation

## create a weave using wolfram cellular automata

def createWeave(width, height, rules):
    # first generate the pattern
    
    pattern = seed(width)
    for i in range(height - 1):
        pattern.append(generate(pattern, rules))
    
    # set up weave
    
    colorTable = { 1: [0, 0, 0], 2: [255, 255, 255] }
    warpThreads = width
    weftThreads = height
    
    # fill weft and warp with black/white
    
    warpColors = []
    for i in range(warpThreads):
        warpColors.append(1)
    
    weftColors = []
    for i in range(weftThreads):
        weftColors.append(2)
    
    # to simulate a Jaquard loom, each thread has its own harness
    
    threading = []
    for i in range(warpThreads):
        threading.append(i + 1)
    
    # each tie-up is unique, so we generate the tie-up as we go
    
    tieUp = {}
    treadling = []
    
    for row in range(len(pattern)):
        harnesses = []
        for x in range(len(pattern[row])):
            if pattern[row][x]:
                harnesses.append(x + 1)
        tieUp[row] = harnesses
        treadling.append(row)
    
    # create weave pattern
    
    weave = Weave(colorTable, warpThreads, weftThreads, tieUp,
                  threading, treadling, warpColors, weftColors)
    return weave
    
    
    

if __name__ == "__main__":
    weave = createWeave(128, 128, [False, False, False, True, True, True, True, False])
    weave.saveBitmap("wolfram.bmp")