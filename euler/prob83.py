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

graph['s'] = {((0, 0), M[0][0])}
	
for i in range(80) :
	for j in range(80) :
		graph[(i,j)] = set()
		if i > 0 : graph[(i, j)].add(((i - 1, j), M[i - 1][j]))
		if j > 0 : graph[(i, j)].add(((i, j - 1), M[i][j - 1]))
		if i < 79 : graph[(i, j)].add(((i + 1, j), M[i + 1][j]))
		if j < 79 : graph[(i, j)].add(((i, j + 1), M[i][j + 1]))
	
begin = ['s']
end = [(79, 79)]

print(shortest_path(graph, begin, end))