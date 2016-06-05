from itertools import count

Found = False
for i in count(1) :
	for j in count(1) :
		if not set(str(j * i)) == set(str(i)) :
			break
		if j > 2 :
			print(i)
		if j >= 6 :
			print(i)
			Found = True
			break
	if Found :
		break