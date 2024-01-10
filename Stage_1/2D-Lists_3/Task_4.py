n = int(input("N: "))
m = int(input("M: "))

lst = [[str(y) for y in range(m)] for x in range(n)]

sty = 0
x = 0
y = 0
i=0
while i < n*m:
    if x < n and y < m:
        lst[x][y] = str(i+1)
    else:
        i-=1
    x += 1
    y -= 1
    if y == -1 or x >= n: 
        sty += 1
        y = sty
        x = 0
    i+=1

for st in lst:
    print(' '.join(st))