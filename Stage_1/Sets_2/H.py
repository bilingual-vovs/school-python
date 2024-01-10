n = int(input())

r = set(str(x) for x in range(1, n))
x = set()
while x != 'HELP':
    if len(r.intersection(x)) > len(r.difference(x)) and x:
        print('YES')
        r = r.intersection(x)
    elif x:
        print('NO')
        r = r.difference(x)
    x = input()
    
    

print(' '.join(sorted(r)))