from math import floor
from integer import pythaTriples

maxM = 1817
total = 0

py1 = pythaTriples(maxM * 3)
py2 = {(a, b, c) for (b, a, c) in py1}

for (ab, c, t) in py1 | py2 :
	for a in range(1, (ab // 2) + 1) :
		b = ab - a
		if c >= a and c >= b and a <= maxM and b <= maxM and c <= maxM :
#			print("For (a, b, c) =", a, ",", b, ",", c, ", the length is", ((a + b)**2 + c**2)**.5)
			total += 1

print(total)
			
#for c in range(1,maxM + 1) :
#	for a in range(1,c + 1) :
#		for b in range(1,a + 1) :
#			length = ((a + b)**2 + c**2)**.5
			#print("For (a, b, c) =", a, ",", b, ",", c, ", the length is", length)
#			if length == floor(length) :
#				print("For (a, b, c) = ({}, {}, {}), length = {}.".format(a,b,c,length))
#				total += 1
				
#print(total)