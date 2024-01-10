n = int(input())
f = [1, 1, 2]
for x in range(2, n):
    f.append(sum(f[x-2:]))
print(f[-1])
