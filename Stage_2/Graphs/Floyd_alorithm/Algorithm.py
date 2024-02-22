class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.matrix = [[False for _ in range(node_count)] for _ in range(node_count)]
        self.weights = []
    
    def add_edge(self, a, b):
        self.matrix[a][b] = self.matrix[b][a] = True

    def add_edge_strict(self, a, b):
        self.matrix[a][b] = True

    def floyd(self):
        n = self.node_count
        for k in range(n):
            self.matrix = [[min(self.matrix[y][x], self.matrix[y][k]*self.weights[k] + self.matrix[k][x]*self.weights[x]) for x in range(n)] for y in range(n)]

inf = float('inf')    

m = [
    [0, 7, 5, 4, inf, inf,],
    [7, 0, 6, 2, inf, inf],
    [5, 6, 0, 3, 8, inf],
    [4, 2, 3, 0, 9, 10],
    [inf, inf, 8, 9, 0, 3],
    [inf, inf, inf, 10, 3, 0]
]
w = [7.3, 5.4, 2.7, 6.2, 9.1, 10]

graph = Graph(6)

graph.matrix = m
graph.weights = w

graph.floyd()
for x in graph.matrix:
    print(x)