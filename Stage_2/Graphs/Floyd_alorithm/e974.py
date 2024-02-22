n = int(input())

m = []
for x in range(n):
    m.append([(int(y) + 1 or float('inf'))-1 for y in input().split()])

for k in range(n):
    m = [[min(m[y][x], m[y][k] + m[k][x]) for x in range(n)] for y in range(n)]

for x in m:
    print(" ".join([str(y) for y in x]))
    