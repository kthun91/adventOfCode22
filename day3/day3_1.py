# https://adventofcode.com/2022/day/1
import os
import string

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    solution = []
    for l in f.readlines():
        part1 = l[0:int(len(l)/2)]
        part2 = l[int(len(l)/2):]
        char = list(set(part1).intersection(part2))
        solution.append(1+string.ascii_letters.find(char[0]))
    print(sum(solution))
