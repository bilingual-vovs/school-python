n = int(input())

m = []

for x in range(n):
    l = [0 for _ in range(n)]
    for y in input().split()[1:]:
        l[int(y)] = 0

print(m)