# https://adventofcode.com/2022
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def topScore(forest, tree, x, y, yCount):
    tmp = []
    if x == 0:
        return 0
    for i in range(0,yCount):
        tmp.append(forest[i][y])
    count = 0
    for e in reversed(tmp[:x]):
        count += 1
        if e >= tree:
            return count
    return count
    
def bottomScore(forest, tree, x, y, yCount):
    tmp = []
    for i in range(0,yCount+1):
        tmp.append(forest[i][y])

    if x == len(tmp)-1:
        return 0
    count = 0
    for e in (tmp[x+1:]):
        count += 1
        if e >= tree:
            return count
    return count

def leftScore(forest, tree, x, y):
    if y == 0:
        return 0
    count = 0
    for e in reversed(forest[x][:y:]):
        count += 1
        if e >= tree:
            return count
    return count

def rightScore(forest, tree, x, y):
    if y == len(forest[x])-1:
        return 0
    count = 0
    for e in (forest[x][y+1:]):
        count += 1
        if e >= tree:
            return count
    return count

def visibleScore(forest, tree, x, y, yCount):
    return topScore(forest, tree, x, y, yCount) * bottomScore(forest, tree, x, y, yCount) * leftScore(forest, tree, x, y) * rightScore(forest, tree, x, y)

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
        res.append(visibleScore(forest, e, i, j, yCount))
print(max(res))
