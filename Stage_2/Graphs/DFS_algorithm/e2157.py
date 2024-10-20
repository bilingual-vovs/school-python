n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n-1):
    i = [int(x) for x in input().split()]
    matrix[i[0]-1][i[1]-1] = matrix[i[1]-1][i[0]-1] = i[2]

node = [0]
edges = []
summ = 0

for x in range(n):
        if matrix[node[-1]][x]:
            for e in range(len(edges)):
                edges[e][1]+=1
            edges.append([matrix[node[-1]][x], 1]) 
            matrix[node[-1]][x] = matrix[x][node[-1]] = 0
            node.append(x)
            break 
        
while len(node) :
    f = False
    for x in range(n):
        if matrix[node[-1]][x]:
            for e in range(len(edges)):
                edges[e][1]+=1
            edges.append([matrix[node[-1]][x], 1]) 
            matrix[node[-1]][x] = matrix[x][node[-1]] = 0
            node.append(x)
            f = True
            break 
    if f: continue
    if len(edges):
        edge = edges.pop(-1)
        summ += edge[0] * edge[1] * (n-edge[1])
    node.pop(-1)
    

    



print(summ)