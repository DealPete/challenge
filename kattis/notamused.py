import sys

CustsEnter = {}
CustsTime = {}

day = 1

for line in sys.stdin:
    if line == "CLOSE\n" or line == "CLOSE":
        print("Day " + str(day))
        keys = list(CustsEnter.keys())
        keys.sort()
        for cust in keys:
            print(cust, '$%.2f' % (CustsTime[cust] * 0.1))
        print("")
        day += 1        
        CustsTime = {}
    elif line != "OPEN\n":
        type, name, time = line.split()
        if type == "ENTER":
            CustsEnter[name] = int(time)
        else:
            time = int(time) - CustsEnter[name]
            if name in CustsTime:
                CustsTime[name] += time
            else:
                CustsTime[name] = time
