inp = input().split()

r = {}
rc = []

for x in inp:
    if x in r: 
        r[x] += 1
    else:
        r[x] = 1
    
for x in r.keys():
    rc.append((len(r) - r[x], x))

rc = sorted(rc)

for x in rc:
    print(x[1])
