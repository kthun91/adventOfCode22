# https://adventofcode.com/2022/day/1
import os
import string

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    solution = []
    lines = []
    counter = 1
    for l in f.readlines():
        lines.append(l[0:-1:])
    for l in lines:
        counter += 1
        if counter % 3 == 0:
            char = list(set(lines[counter-1]).intersection(lines[counter-2]))
            char2 = list(set(char).intersection(lines[counter-3]))
            solution.append(1+string.ascii_letters.find(char2[0]))
    print(sum(solution))
