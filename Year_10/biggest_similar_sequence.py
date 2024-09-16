a = input().split()
b = input().split()

m = []
for i in range(len(a)):
    ml = []
    for j in range(len(b)):
        if min(i,j) == 0: ml.append(0)
        elif a[i] == b[j]: ml.append(m[i-1][j-1]+1)
        else: ml.append(max(m[i-1][j], ml[j-1]))
    m.append(ml)

s = []
i = j = -1
for x in range(m[-1][-1]):
    if a[i] == b[j]: 
        s.append(a[i])
        i -= 1
        j -= 1
    elif m[i-1][j] > m[i][j-1]:
        s.append(a[i])
        i-=1
    else:
        s.append(b[j])
        j-=1
for x in m:
    print(x)

print(s)