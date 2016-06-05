num = 3
denom = 2

total = 0

for i in range(1, 999) :
	num += denom
	num, denom = denom, num
	num += denom
	
	if len(str(num)) > len(str(denom)) :
		total += 1
	
#	print("{}/{}".format(num, denom))
	
print(total)