# https://adventofcode.com/2022
import os
from pprint import pprint

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def top(forest, tree, x, y, yCount):
    tmp = []
    for i in range(0,yCount):
        tmp.append(forest[i][y])
    if x == 0:
        return True
    return tree > max(tmp[:x])
    
def bottom(forest, tree, x, y, yCount):
    tmp = []
    for i in range(0,yCount+1):
        tmp.append(forest[i][y])
    if len(tmp) == x+1:
        return True
    return tree > max(tmp[x+1:])

def left(forest, tree, x, y):
    if y == 0:
        return True
    return tree > max(forest[x][:y])

def right(forest, tree, x, y):
    if len(forest[x]) == y+1:
        return True
    return tree > max(forest[x][y+1:])

def visible(forest, tree, x, y, yCount):
    return top(forest, tree, x, y, yCount) or bottom(forest, tree, x, y, yCount) or left(forest, tree, x, y) or right(forest, tree, x, y)

with open(abs_file_path, "r") as g:
    xCount = 0
    yCount = 0
    for i, l in enumerate(g.readlines()):
        for j, e in enumerate(l[:-1]):
            xCount = j # 5
            yCount = i

with open(abs_file_path, "r") as f:
    forest = [[0 for x in range(xCount+1)] for y in range(yCount+1)] 
    for i, l in enumerate(f.readlines()):
        for j, e in enumerate(l[:-1]):
            forest[i][j] = int(e)

res = []
for i, f in enumerate(forest):
    for j, e in enumerate(f):
        res.append(visible(forest, e, i, j, yCount))
print(sum(res))
