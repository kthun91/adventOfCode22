# https://adventofcode.com/2022/day/1
import os
import itertools

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def compareSubString(subString):
    if len(subString) != 14:
        return False
    compareList = []
    for a, b in itertools.combinations(subString, 2):
        compareList.append(a == b)
    return sum(compareList) # returns number of dublicates

with open(abs_file_path, "r") as f:
    inp = f.readline()
    for i in range(0,len(inp)):
        if not compareSubString(inp[i:i+14:]):
            print(inp[i:i+14:])
            print(i+14)
            break