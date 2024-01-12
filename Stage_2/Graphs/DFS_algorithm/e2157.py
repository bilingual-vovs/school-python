n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

counters = [0 for _ in range(n)]

for _ in range(n-1):
    i = [int(x) for x in input().split()]
    matrix[i[0]-1][i[1]-1] = matrix[i[1]-1][i[0]-1] = i[2]

    counters[i[0]-1] += 1
    counters[i[1]-1] += 1

for x in range(n):
    if counters[x] == 1:
        corner = x
        break

path = [corner]
suma = 0
for x in range(n):
        edge = matrix[path[-1]][x]
        if edge and type(edge) is int:
            matrix[x][path[-1]] = [edge, len(path)]
            path.append(x)

while path[-1] != corner :
    aded = False
    for x in range(n):
        edge = matrix[path[-1]][x]
        if edge and type(edge) is int:
            matrix[x][path[-1]] = [edge, len(path)+1]
            path.append(x)
            aded = True
    if not aded:
        matrix[path[-2]][path[-1]] = [matrix[path[-2]][path[-1]], len(path)-1]
        path.pop(-1)



for x in matrix:
    print(x)