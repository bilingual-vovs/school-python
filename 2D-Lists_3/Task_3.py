n = int(input("N: "))
m = int(input("M: "))

c = 0
for x in range(n):
    toPrint = []
    for y in range(m):
        c+=1
        toPrint.append(str(c))
    print(' '.join(toPrint))