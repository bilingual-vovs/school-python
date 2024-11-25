n = int(input())

if n == 0:
    print(0)
else:

    def minN(ln):
        r = 1
        i = 1
        while r+i <= ln:
            r+=i
            i+=1
        return i

    b = [minN(x) for x in range(1,n+2)]

    m = [[0 for _ in range(n+1)] for _ in range(n+1)]

    
    if n >= 1: m[1][1] = 1
    if n >= 2:    m[2][2] = 1
    m[0][0] = 1

    for ln in range(2,n+1):
        for bs in range(b[ln-1],ln+1):
            g = m[n-bs][slice(0, bs)]
            m[ln][bs] = sum(m[ln-bs][slice(0, bs)])
    print(sum(m[-1]))      