from algebra import permute

l = [i for i in range(9,0,-1)]

for z in permute(l) :
	
	i = ""
	for p in z :
		i += str(p)
	i = int(i)
	
	found = True
	s = str(i)
	j = int(s[0:4])
	k = j

	while len(s) >= len(str(k)) and found == True :
		if s[0:len(str(k))] == str(k) :
			s = s[len(str(k)):]
			k += j
		else :
			found = False
		
	if found == True and len(s) == 0 :
		print("Found the largest:  i =", i, " j =", j)
		break
	
	print(i, "is not such a pandigital number.")
	