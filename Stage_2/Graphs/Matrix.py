class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.matrix = [[False for _ in range(node_count)] for _ in range(node_count)]
    
    def add_edge(self, a, b):
        self.matrix[a][b] = self.matrix[b][a] = True

    def add_edge_strict(self, a, b):
        self.matrix[a][b] = True

    def get_list(self):
        res_list = [[] for _ in range(self.node_count)]
        for y in range(self.node_count):
            for x in range(self.node_count):
                if self.matrix[x][y]:
                    res_list[x].append(y)

        return res_list
    

graph = Graph(5)
graph.add_edge(0, 2)
graph.add_edge_strict(4, 3)
graph.add_edge_strict(3, 1)
graph.add_edge(1, 0)
print(graph.get_list())