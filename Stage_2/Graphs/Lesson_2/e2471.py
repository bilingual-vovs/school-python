n = int(input())

l = []
for y in range(n):
    inp = input().split()
    for x in range(n):
        if inp[x] == '1':
            a = (min(x, y)+1, max(x, y)+1)
            if not a in l: l.append(a)
    
for x in l:
    print(f'{x[0]} {x[1]}')

