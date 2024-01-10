n = int(input())
m = int(input())

g = [[x*n+(n-y-1) for x in range(m)] for y in range(n)]

for r in g:
    print('\t'.join(map(str, r)))