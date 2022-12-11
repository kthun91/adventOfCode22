# https://adventofcode.com/2022
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# abs(y1 - y2) <= 1 and abs(x1 - x2)
def inRange(h, t):
    return (h['xPos']-1 == t['xPos'] or
            h['xPos'] == t['xPos'] or
            h['xPos']+1 == t['xPos']) and (
            h['yPos']-1 == t['yPos'] or
            h['yPos'] == t['yPos'] or
            h['yPos']+1 == t['yPos']
            )    

def moveRight(h, t):
    h['xPos'] = h['xPos'] + 1
    if not inRange(h ,t):
        t['xPos'] = h['xPos'] - 1
        t['yPos'] = h['yPos']
    return h, t

def moveLeft(h, t):
    h['xPos'] = h['xPos'] - 1
    if not inRange(h ,t):
        t['xPos'] = h['xPos'] + 1
        t['yPos'] = h['yPos']
    return h, t

def moveUp(h, t):
    h['yPos'] = h['yPos'] + 1
    if not inRange(h ,t):
        t['xPos'] = h['xPos']
        t['yPos'] = h['yPos'] - 1
    return h, t

def moveDown(h, t):
    h['yPos'] = h['yPos'] - 1
    if not inRange(h ,t):
        t['xPos'] = h['xPos']
        t['yPos'] = h['yPos'] + 1
    return h, t

def move(head, tail, direction, steps):
    visited = [[tail['xPos'], tail['yPos']]]
    if direction == "R":
        for i in range(0, steps):
            moveRight(head, tail)
            visited.append([tail['xPos'], tail['yPos']])
    if direction == "L":
        for i in range(0, steps):
            moveLeft(head, tail)
            visited.append([tail['xPos'], tail['yPos']])
    if direction == "U":
        for i in range(0, steps):
            moveUp(head, tail)
            visited.append([tail['xPos'], tail['yPos']])
    if direction == "D":
        for i in range(0, steps):
            moveDown(head, tail)
            visited.append([tail['xPos'], tail['yPos']])
    return visited

def unique(visited):
    newVisited = []
    for e in visited:
        if e not in newVisited:
            newVisited.append(e)
    return newVisited

with open(abs_file_path, "r") as f:
    head, tail = {"xPos": 0,"yPos": 0}, {"xPos": 0,"yPos": 0}
    directions = []
    visited = [[tail['xPos'], tail['yPos']]]
    for c in f.readlines():
        directions.append(c[:-1])
    #print(directions)
    for d in directions:
        visited.extend(move(head, tail, d.split()[0], int(d.split()[1])))
    print(len(unique(visited)))

