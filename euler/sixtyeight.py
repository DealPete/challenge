from algebra import permute

l = [x for x in range(1,11)]

p = []

t = 14

for m in permute(l) :
	if m[0] + m[2] + m[3] == t and m[1] + m[3] + m[7] == t and m[2] + m[4] + m[5] == t and m[6] + m[7] + m[8] == t and m[4] + m[6] + m[9] == t :
		p.append(m)

for m in p :
	print(m[0],m[2],m[3],';',m[1],m[3],m[7],';',m[8],m[7],m[6],';',m[9],m[6],m[4],';',m[5],m[4],m[2])
