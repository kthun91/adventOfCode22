# https://adventofcode.com/2022/day/1
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def compareSubString(subString):
    if len(subString) != 4:
        return False
    return subString[0] != subString[1] and subString[0] != subString[2] and subString[0] != subString[3] and subString[1] != subString[2] and subString[1] != subString[3] and subString[2] != subString[3]

with open(abs_file_path, "r") as f:
    inp = f.readline()
    for i in range(0,len(inp)):
        if compareSubString(inp[i:i+4:]):
            print(inp[i:i+4:])
            print(i+4)
            break