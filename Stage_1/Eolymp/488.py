def solutin(n):
    r2 = []
    for x in range(n):
        r1 = []
        for y in range(n):
            if x%2 == 0:
                r1.append(x*n+y+1)
            else:
                r1.append(n*(x+1)-y)
        r2.append(r1)
    return r2

