import sys

lines = sys.stdin.readlines()

dimY, dimX, expY, expX = map(int, lines[0].split())

for y in range(0, dimY):
    for j in range(0, expY):
        line = "" 
        for x in range(0, dimX):
            line += lines[y + 1][x] * expX
        print(line)


        
