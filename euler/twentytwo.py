f = open('names.txt')

s = f.read()
l = list()

tempstr = ""

for ch in s :
	if ch not in {'"',','} :
		tempstr += ch
	elif tempstr :
		l.append(tempstr)
		tempstr = ""
		
l.sort()

x, t = 0, 0

while x < len(l) :
	str = l[x]
	for ch in str :
		t += (ord(ch) - 64) * (x + 1)
	
	x += 1
	
print(t)
