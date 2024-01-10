n = int(input())

d = {}
for x in range(n):
    inp = input().split(' - ')
    for y in inp[1].split(', '):
        d[y] = inp[0]

print(d)

for x in d.keys():
    print(f'{x} - {d[x]}')