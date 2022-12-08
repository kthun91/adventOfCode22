# https://adventofcode.com/2022
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    commands = []
    myDict = {}
    stack = []

    for l in f.readlines():
        commands.append(l[:-1])
    for c in commands:
        if "$ cd " in c and "$ cd .." not in c:
            stack.append(str(stack) + c.split()[2]) # for unique name or some sort of path
        if c.split()[0].isdigit():
            for s in stack:
                if s not in myDict:
                    myDict[s] = 0
                myDict[s] += int(c.split()[0])
        if "$ cd .." in c:
            stack.pop()

    res = 0
    for e in myDict:
        if myDict.get(e) < 100_001:
            res += myDict.get(e)
    print(res)
