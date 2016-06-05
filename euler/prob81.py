f = open('p081_matrix.txt')

M = []
l = f.readline()

while l :
	if l[-1] == '\n' :
		l = l[:-1]
	m = l.split(sep=',')
	M.append([int(x) for x in m])
	l = f.readline()

f.close()

SP = [[[] for x in range(80)] for x in range(80)]

SP[79][79] = M[79][79]

for i in range(78, -1, -1) :
	SP[i][79] = M[i][79] + SP[i + 1][79]
	
for j in range(78, -1, -1) :
	SP[79][j] = M[79][j] + SP[79][j + 1]
	
for i in range(78, -1, -1) :
	for j in range(78, -1, -1) :
		SP[i][j] = M[i][j] + min(SP[i+1][j], SP[i][j+1])

print(SP[0][0])