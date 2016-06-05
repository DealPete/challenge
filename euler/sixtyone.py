n = [[],[],[],[],[],[]]
ans = []


for i in range(1, 200) :
	n[0].append(i*(i+1)//2)
	n[1].append(i*i)
	n[2].append(i*(3*i - 1)//2)
	n[3].append(i*(2*i - 1))
	n[4].append(i*(5*i - 3)//2)
	n[5].append(i*(3*i - 2))

for i in range(6) :
	n[i] = [x for x in n[i] if x > 999 and x < 10000]
	print(n[i])

	
def search(q, k) :
	print("{} ->".format(k), end="")
	global ans
	global c
	if q == [] :
		if k % 100 == c // 100 :
			ans = [k] + ans
			return True
		else :
			return False
	for i in q :
		for j in i :
			if j // 100 == k % 100 :
				if search([x for x in q if x != i], j) :
					ans = [j] + ans
					print("found something!!")
					return True
	print(" X")
	return False
	

for c in n[0] :
	if search([n[1], n[2], n[3], n[4], n[5]], c) :
#		if (ans[4] % 100 == c // 100) :
		print("The answer is {} -> {} -> {} -> {} -> {} -> {}".format(c, ans[0], ans[1], ans[2], ans[3], ans[4]))
		break
#	wait = input("PRESS ENTER TO CONTINUE.")