class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.matrix = [[False for _ in range(node_count)] for _ in range(node_count)]
    
    def add_edge(self, a, b, c = 1):
        self.matrix[a][b] = self.matrix[b][a] = c

    def add_edge_strict(self, a, b, c = 1):
        self.matrix[a][b] = c

    def get_list(self):
        res_list = [[] for _ in range(self.node_count)]
        for y in range(self.node_count):
            for x in range(self.node_count):
                if self.matrix[x][y]:
                    res_list[x].append(y)
        return res_list

    def bake_dej(self, start):
        dejlist = [float('inf') for x in range(self.node_count)]
        dejlist[start] = 0
        dejfix = [-1 for x in range(self.node_count)]
        dejfix[start] = 0
        act = start

        for x in range(self.node_count-1):
            for y in range(self.node_count):
                if self.matrix[act][y] and dejfix[y] == -1:
                    dejlist[y] = min(dejlist[y], dejfix[act] + self.matrix[act][y]-1)
            i = 0
            minm = float('inf')
            for y in range(self.node_count):
                if minm > dejlist[y] and dejfix[y] == -1:
                    indx = y
                    minm = dejlist[y]
                i+=1
            act = indx
            dejfix[act] = minm
        return dejfix

inp = input().split()                

graph = Graph(int(inp[0]))

matrix = []
for x in range(int(inp[0])):
    matrix.append([int(y)+1 for y in input().split()])

graph.matrix = matrix

print(graph.bake_dej(int(inp[1])-1)[int(inp[2])-1])
