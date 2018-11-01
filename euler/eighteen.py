f = open('triangle.txt')

l = f.readline()
line = []

while l :
	subline = []
	while l :
		subline.append(int(l[:2]))
		l = l[3:]
	line.append(subline)
	l = f.readline()

t = [line[0]]

t.append([line[1][0] + line[0][0], line[1][1] + line[0][0]])

for row in line[2:]:
	compare = t[-1]
	u = [compare[0] + row[0]]
	for x in range(1, len(row) - 1) :
		u.append(row[x] + max(compare[x - 1], compare[x]))
	u.append(compare[-1] + row[-1])
	t.append(u)
	
print(t)
