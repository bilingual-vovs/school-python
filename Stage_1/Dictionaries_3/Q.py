n = int(input())

c = {}

for _ in range(n):
    inp = input().split(", ")
    cl = False
    s = []
    for x in inp:
        for y in x.split():
            c[y] = cl or 'It is a country'
            cl = cl or y
    
m = int(input())

stack = []
for _ in range(m):
    stack.append(input())

for x in stack:
    print(c[x])