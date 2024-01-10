n = int(input())

l = []
for y in range(n):
    inp = input().split()
    for x in range(n):
        if inp[x] == '1':
            l.append(y, x)
    
for x in l:
    print(f'{x[0]} {x[1]}')

