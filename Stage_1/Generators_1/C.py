n = int(input())
m = int(input())

g = [[y*m+x for x in range(m)] for y in range(n)]

for r in g:
    print('\t'.join(map(str, r)))