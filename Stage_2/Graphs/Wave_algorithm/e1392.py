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
        self.bakemap[start] = 1
        self.bake_node_children(start, 2)
        i = 2
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
                
inp = input().split()

graph = Graph(int(inp[0]))

for x in range(int(inp[1])):
    i = input().split()
    graph.add_edge(int(i[0])-1, int(i[1])-1)

graph.bake_wave(int(inp[2])-1)

l=[]
i=0
for x in graph.bakemap:
    i+=1
    if x:
        l.append((str(x+1), str(i)))
r = []
for x in sorted(l):
    r.append(x[1])
print(len(r))
print(" ".join(r))


