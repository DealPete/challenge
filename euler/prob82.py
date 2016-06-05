from graph import shortest_path

f = open('p081_matrix.txt')

graph = {}

M = []
l = f.readline()

while l :
	if l[-1] == '\n' :
		l = l[:-1]
	m = l.split(sep=',')
	M.append([int(x) for x in m])
	l = f.readline()
	
f.close()

for x in range(80) :
	graph['s' + str(x)] = {((x, 0), M[x][0])}
	
for x in range(79) :
	graph[(0, x)] = {((1, x), M[1][x]), ((0, x + 1), M[0][x + 1])}
	graph[(79, x)] = {((78, x), M[78][x]), ((79, x + 1), M[79][x + 1])}
	for y in range(1, 79) :
		graph[(y, x)] = {((y + 1, x), M[y + 1][x]), ((y - 1, x), M[y - 1][x]), ((y, x + 1), M[y][x + 1])}

for x in range(80) :
	graph[(x, 79)] = {}
	
begin = ['s' + str(x) for x in range(80)]
end = [(x, 79) for x in range(80)]

print(shortest_path(graph, begin, end))