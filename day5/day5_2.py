# https://adventofcode.com/2022/day/1
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path_crates = "crates.txt"
abs_file_path_crates = os.path.join(script_dir, rel_path_crates)
rel_path_input = "input.txt"
abs_file_path_input = os.path.join(script_dir, rel_path_input)

def getCrates(abs_file_path_crates):
    with open(abs_file_path_crates, "r") as f:
        crates = []
        tmp_crates = []
        for l in f.readlines():
            crates.append(l[:-1].replace('   ', ' [0]'))
        for c in crates:
            items = c.split(' ')
            tmp_crates.append(items)
        tmp_crates2 = []
        for cra in tmp_crates:
            xs = [x for x in cra if x != '']
            tmp_crates2.append(xs)
        crates = list(map(list, zip(*reversed(tmp_crates2[:-1]))))
        final_crates = []
        for cr in crates:
            xs = [x for x in cr if x != '[0]']
            final_crates.append(xs)
        return final_crates

def moveCrates(crates, quantity, origin, destination):
    new_crates = crates.copy()
    new_crates[origin - 1] = crates[origin - 1][:-quantity]
    for x in crates[origin - 1][len(crates[origin - 1]) - quantity:]:
        new_crates[destination - 1].append(x)
    return new_crates

crates = getCrates(abs_file_path_crates)
print(crates)
with open(abs_file_path_input, "r") as f:
    for l in f.readlines():
        nums = [int(s) for s in l.split() if s.isdigit()]
        crates = moveCrates(crates, nums[0], nums[1], nums[2])
solution = []
for e in crates:
    solution.append(e[-1].replace('[','').replace(']',''))
print(''.join(solution))
