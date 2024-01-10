n = int(input())

r = False
for y in range(n):
    inp = input().split()
    for x in range(n):
        if x == y and inp[x] == '1':
            r = True
    
if r:
    print("YES")
else:
    print('NO')

