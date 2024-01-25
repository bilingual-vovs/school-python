import random
# inp = input().split()
while True:
    n = random.randint(1, 200)
    s = random.randint(1, n-1)
    to = random.randint(1, n-1)

    matrix = []
    for _ in range(n):
        matrix.append([random.choices([random.randint(0, n), -1], weights=(30, 70), k=2)[0] + 1 for x in range(n)])


    dejlist = [float('inf') for x in range(n)]
    dejlist[s] = 0
    dejfix = [-1 for x in range(n)]
    dejfix[s] = 0
    act = s

    for _ in range(n-1):
        for y in range(n):
            if matrix[act][y] and dejfix[y] == -1:
                dejlist[y] = min(dejlist[y], dejfix[act] + matrix[act][y]-1)
        indx = 'f'
        minm = float('inf')
        for y in range(n):
            if minm > dejlist[y] and dejfix[y] == -1:
                minm = dejlist[y]
                indx = y
        if indx != 'f':
            act = indx
            dejfix[act] = minm

    print(n, s, to ,dejfix[to])

