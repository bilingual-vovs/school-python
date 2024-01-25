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
                    dejlist[y] = min(dejlist[y], dejfix[act] + self.matrix[act][y])
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
            

                    




                

graph = Graph(6)
graph.add_edge_strict(0, 2, 1)
graph.add_edge_strict(0, 1, 2)
graph.add_edge_strict(0, 3, 4)
graph.add_edge_strict(2, 4, 10)
graph.add_edge_strict(2, 3, 5)
graph.add_edge_strict(2, 5, 4)
graph.add_edge_strict(1, 3, 7)
graph.add_edge_strict(1, 4, 2.5)
graph.add_edge_strict(3, 5, 5)
graph.add_edge_strict(4, 5, 4)

print(graph.bake_dej(0))
