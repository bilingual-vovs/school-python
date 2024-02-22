n = int(input())

m = []
for x in range(n):
    m.append([(int(y) or float('inf')) for y in input().split()])

for k in range(n):
    m = [[min(m[y][x], m[y][k] + m[k][x]) for x in range(n)] for y in range(n)]

for x in range(n):
    print(" ".join(['0' if y == float('inf') else '1' if y > 0 else '2' for y in m[x]]))