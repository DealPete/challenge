from algebra import permute

l = [i for i in range(1, 10)]

for i in permute(l) :
	j = str(i[0]) + str(i[1])
	k = str(i[2]) + str(i[3]) + str(i[4])
	m = str(i[5]) + str(i[6]) + str(i[7]) + str(i[8])
	
	if int(j) * int(k) == int(m) :
		print(j, "x", k, "=", m)
		
	j = str(i[0])
	k = str(i[1]) + str(i[2]) + str(i[3]) + str(i[4])
	
	if int(j) * int(k) == int(m) :
		print(j, "x", k, "=", m)