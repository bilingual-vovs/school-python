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

    def bake_bfs(self, start):
        self.list = self.get_list()
        self.stack = []
        self.bakemap = [False for _ in range(self.node_count)]
        self.bakemap[start] = 1
        self.bake_node_children([2, start])
        while len(self.stack):
            self.bake_node_children(self.stack[0])
            self.stack.pop(0)

        
    
    def bake_node_children(self, node_data):
        for x in self.list[node_data[1]]:
            if not self.bakemap[x]:
                self.bakemap[x] = node_data[0]
                self.stack.append([node_data[0]+1, x])
    
    def find_path_length(self, a, b):
        self.bake_bfs(a)
        return self.bakemap[b] - 1


                

graph = Graph(4)
graph.add_edge(0, 3)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(0, 2)

print(graph.find_path_length(3, 2))
print(graph.bakemap)