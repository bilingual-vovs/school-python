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

    def bake_wave(self, start):
        self.list = self.get_list()
        self.bakemap = [False for _ in range(self.node_count)]
        self.bakemap[start] = 0
        self.bake_node_children(start, 1)
        i = 1
        j = 1 
        while j != 0:
            j=0
            i+=1
            for x in range(self.node_count):
                if self.bakemap[x] == i-1:
                    j+=1
                    self.bake_node_children(x, i)
    
    def bake_node_children(self, node, i):
        for x in self.list[node]:
            if not self.bakemap[x]:
                self.bakemap[x] = i
                

graph = Graph(5)
graph.add_edge(0, 2)
graph.add_edge_strict(4, 3)
graph.add_edge_strict(3, 0)
graph.add_edge(1, 0)

graph.bake_wave(4)
print(graph.bakemap)
print(graph.get_list())