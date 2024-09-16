[n, m] = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]
mx = []
for x in range(n):
    if x in l: mx.append(0)
    elif x == 1: x = 1
    else: mx.append(sum([mx[x-y-1] for y in range(min(x, 3))]))


for x in range(n):
    if mx[x] == 0: mx[x] = -1

print(mx)