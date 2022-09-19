def solution(m, n, x, y):
    r = []
    if x-1>=1:
        r.append([x-1, y])
    if y-1>=1:
        r.append([x, y-1])
    if x+1<=m:
        r.append([x+1, y])
    if y+1<=n:
        r.append([x, y-1])
    return r    

