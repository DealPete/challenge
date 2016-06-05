from integer import triangles

f = open(".\Euler\words.txt")

w = [n.strip('"') for n in f.read().split(",")]

tri = triangles(20)
t = 0

for n in w :
	st = 0
	for ch in n :
		st += ord(ch) - 64
	if st in tri :
		t += 1

print(t)