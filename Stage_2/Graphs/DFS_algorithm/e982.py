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

    def dfs(self, start):
        self.found = [start]
        self.find_next(start)

    def find_next(self, node):
        for x in range(self.node_count):
            if self.matrix[node][x] and not x in self.found:
                self.found.append(x)
                if self.find_next(x):
                    return self.find_next(node)
        return False

        
inp = input().split()

graph = Graph(int(inp[0]))

for x in range(int(inp[1])):
    i = input().split()
    graph.add_edge(int(i[0])-1, int(i[1])-1)

graph.dfs(0)

if len(graph.found) == int(inp[0]):
    print("YES")
else:
    print("NO")
