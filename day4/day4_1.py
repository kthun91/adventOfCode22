# https://adventofcode.com/2022/day/1
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def extend(line):
    firstElf = []
    secondElf = []
    elfes = line[:-1].split(',')
    # first elf
    elfRange = elfes[0].split('-')
    for i in range(int(elfRange[0]),int(elfRange[1])+1):
        firstElf.append(i)
    # second elf
    elfRange = elfes[1].split('-')
    for i in range(int(elfRange[0]),int(elfRange[1])+1):
        secondElf.append(i)
    return [firstElf, secondElf]

def includes(listOfElfes):
    intersec = list(set(listOfElfes[0]).intersection(listOfElfes[1]))
    return len(intersec) == len(listOfElfes[0]) or len(intersec) == len(listOfElfes[1])

with open(abs_file_path, "r") as f:
    counter = 0
    for l in f.readlines():
        if includes(extend(l)):
            counter += 1
    print(counter)