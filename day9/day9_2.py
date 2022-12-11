# https://adventofcode.com/2022
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def adjustRange(knots):
    for i, h in enumerate(knots[:-1]):
        if knots[i+1]['xPos'] == h['xPos'] and h['yPos'] + 2 == knots[i+1]['yPos']:
            knots[i+1]['yPos'] -= 1
        if h['xPos'] == knots[i+1]['xPos'] and knots[i+1]['yPos'] + 2 == h['yPos']:
            knots[i+1]['yPos'] += 1
        if knots[i+1]['yPos'] == h['yPos'] and h['xPos'] + 2 == knots[i+1]['xPos']:
            knots[i+1]['xPos'] -= 1
        if h['yPos'] == knots[i+1]['yPos'] and knots[i+1]['xPos'] + 2 == h['xPos']:
            knots[i+1]['xPos'] += 1 
        if (h['xPos'] == knots[i+1]['xPos'] -2 and h['yPos'] == knots[i+1]['yPos'] +1) or (h['xPos'] == knots[i+1]['xPos'] -1 and h['yPos'] == knots[i+1]['yPos'] +2) or (h['xPos'] == knots[i+1]['xPos'] -2 and h['yPos'] == knots[i+1]['yPos'] +2):
            knots[i+1]['xPos'] -=1
            knots[i+1]['yPos'] +=1
        if (h['xPos'] == knots[i+1]['xPos'] +1 and h['yPos'] == knots[i+1]['yPos'] +2) or (h['xPos'] == knots[i+1]['xPos'] +2 and h['yPos'] == knots[i+1]['yPos'] +1) or (h['xPos'] == knots[i+1]['xPos'] +2 and h['yPos'] == knots[i+1]['yPos'] +2):
            knots[i+1]['xPos'] +=1
            knots[i+1]['yPos'] +=1
        if (h['xPos'] == knots[i+1]['xPos'] +2 and h['yPos'] == knots[i+1]['yPos'] -1) or (h['xPos'] == knots[i+1]['xPos'] +1 and h['yPos'] == knots[i+1]['yPos'] -2) or (h['xPos'] == knots[i+1]['xPos'] +2 and h['yPos'] == knots[i+1]['yPos'] -2):
            knots[i+1]['xPos'] +=1
            knots[i+1]['yPos'] -=1
        if (h['xPos'] == knots[i+1]['xPos'] -1 and h['yPos'] == knots[i+1]['yPos'] -2) or (h['xPos'] == knots[i+1]['xPos'] -2 and h['yPos'] == knots[i+1]['yPos'] -1) or (h['xPos'] == knots[i+1]['xPos'] -2 and h['yPos'] == knots[i+1]['yPos'] -2):
            knots[i+1]['xPos'] -=1
            knots[i+1]['yPos'] -=1
    return knots

def moveRight(knots):
    knots[0]['xPos'] = knots[0]['xPos'] + 1
    adjustRange(knots)
    return knots

def moveLeft(knots):
    knots[0]['xPos'] = knots[0]['xPos'] - 1
    adjustRange(knots)
    return knots

def moveUp(knots):
    knots[0]['yPos'] = knots[0]['yPos'] + 1
    adjustRange(knots)
    return knots

def moveDown(knots):
    knots[0]['yPos'] = knots[0]['yPos'] - 1
    adjustRange(knots)
    return knots

def move(knots, direction, steps):
    visited = [[knots[9]['xPos'], knots[9]['yPos']]]
    if direction == "R":
        for _ in range(steps):
            moveRight(knots)
            visited.append([knots[9]['xPos'], knots[9]['yPos']])
    if direction == "L":
        for _ in range(steps):
            moveLeft(knots)
            visited.append([knots[9]['xPos'], knots[9]['yPos']])
    if direction == "U":
        for _ in range(steps):
            moveUp(knots)
            visited.append([knots[9]['xPos'], knots[9]['yPos']])
    if direction == "D":
        for _ in range(steps):
            moveDown(knots)
            visited.append([knots[9]['xPos'], knots[9]['yPos']])
    return visited

def unique(visited):
    newVisited = []
    for e in visited:
        if e not in newVisited:
            newVisited.append(e)
    return newVisited

with open(abs_file_path, "r") as f:
    knots = [{"xPos": 0,"yPos": 0} for _ in range(10)]
    directions = []
    visited = [[knots[9]['xPos'], knots[9]['yPos']]]
    for c in f.readlines():
        directions.append(c[:-1])
    for d in directions:
        visited.extend(move(knots, d.split()[0], int(d.split()[1])))       
    print(len(unique(visited)))

