import random

def seed(width, probability = 0.5):
    pattern = []
    pattern.append([])
    
    for x in range(width):
        if random.random() < probability:
            pattern[0].append(True)
        else:
            pattern[0].append(False)
    
    return pattern

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
    
    pattern.append(generation)
    return pattern

if __name__ == "__main__":
    pattern = seed(128)
    for i in range(128):
        pattern = generate(pattern, [False, False, False, True, True, True, True, False])
    
    for row in pattern:
        line = ""
        for column in row:
            if column:
                line += "*"
            else:
                line += " "
        print(line)