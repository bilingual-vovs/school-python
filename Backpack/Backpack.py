inp = input().split()
ic = int(inp[0])
bcm = int(inp[1])

cList = []
for _ in range(ic):
    g =input().split()
    cList.append([int(g[0]), int(g[1])])


wList = []
iList = []
for w in range(bcm):
    iList = [0]
    i = 1
    for a in cList: 
        iList.append(max(a[0] + iList[i-1] * (bcm - a[1]), iList[i-1] * bcm))
        i+=1
    wList.append(iList)
print(wList)