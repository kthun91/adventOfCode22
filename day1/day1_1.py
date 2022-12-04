# https://adventofcode.com/2022/day/1
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    listOfElves = []
    totalCalories = 0
    for l in f.readlines():
        if l == "\n":
            listOfElves.append(totalCalories)
            totalCalories = 0
            continue
        totalCalories += int(l)
    print(max(listOfElves))