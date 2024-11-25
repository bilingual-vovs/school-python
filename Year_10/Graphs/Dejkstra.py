n = int(input())

m = [[int(x) if x != '10000' or x != '0' else float('-inf') for x in input().split()] for _ in range(n)]

v = [False for _ in range(n)]
d = [float('-inf') for _ in range(n)]
s = 0
v[s] = True
d[s] = 0

for _ in range(n-1):
    t = [(m[s][x], x) for x in range(n) if m[s][x] != float('-inf')]
    mn = min(t)
    d[mn[1]] = d[s] + mn[0]
    s = mn[1]
    v[s] = True

print(d)


