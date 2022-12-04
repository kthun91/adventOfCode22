# https://adventofcode.com/2022/day/1
import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)
# rock lost scissors 3+0
# rock draw rock 1+3
# rock win paper 2+6
# paper lost rock 1+0
# paper draw paper 2+3
# paper win scissors 3+6
# scissors lost paper 2+0
# scissors draw scissors 3+3
# scissors win rock 1+6
dict = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7
}

with open(abs_file_path, "r") as f:
    score = 0
    for l in f.readlines():
        score += dict[l]
    print(score)