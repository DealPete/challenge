f = open('cipher1.txt')

s = f.read()

l = s.split(',')
l[-1] = l[-1].rstrip('\n')

code = [103, 111, 100]

n = 0
j = 0
for i in l :
	n += int(i) ^ code[j % 3]
	print(chr(int(i) ^ code[j % 3]), end="")
	j += 1
	
print("\n{}".format(n))

#for i in range(2, len(l), 3) :
#	k.append(int(l[i]))

	
#def decode(n) :
#	for i in k :
#		print(chr(i ^ n),end="")