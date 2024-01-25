inp = input().split()
n = int(inp[0])
to = int(inp[1])
s = 0

matrix = []
for _ in range(n):
    matrix.append([int(x) if x != '10000' else 0 for x in input().split(' ')])


dejlist = [float('inf') for _ in range(n)]
dejlist[s] = 0
dejfix = [-1 for _ in range(n)]
dejfix[s] = 0
act = s 

for x in range(n-1):
    for y in range(n):
        if matrix[act][y] and dejfix[y] == -1:
            dejlist[y] = min(dejlist[y], dejfix[act] + matrix[act][y])
    minm = float('inf')
    for y in range(n):
        if minm > dejlist[y] and dejfix[y] == -1:
            minm = dejlist[y]
            indx = y
    act = indx
    dejfix[act] = minm

print(dejfix[to-1])