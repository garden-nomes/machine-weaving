
import random

def pickColor():

    colorInput1 = raw_input('Please enter color : ')

    if colorInput1 == 'red':
        color1 = str((random.randint(100, 255), random.randint(0, 100), random.randint(0, 100)))
    if colorInput1 == 'blue':
        color1 = str((random.randint(0, 100), random.randint(0, 100), random.randint(100, 255)))
    if colorInput1 == 'green':
        color1 = str((random.randint(0, 100), random.randint(100, 255), random.randint(0, 100)))

    print(color1)

    return color1
