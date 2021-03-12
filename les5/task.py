# task 1 = def convert(weightOnEarth)
# input weight from keyboard

# create method with 2 parameters def power2(number, stepen)
# 2^4 = 16, 2 * 2 * 2 * 2

import sys

def convert(weightOnEarth):
    weightOnMars = weightOnEarth / 2.64
    print("Weight %s on Mars: %s" % (weightOnEarth, weightOnMars) )

print("Input your weight on Earth: ")
weightOnEarth = int(sys.stdin.readline())
convert(weightOnEarth)