n = int(input())

m = [1, 1, 2]

for x in range(3,n+1):
    m.append(m[x-1]+m[x-2]+m[x-3])

print(m[n])