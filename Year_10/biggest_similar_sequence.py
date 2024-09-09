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


for x in m:
    print(x)