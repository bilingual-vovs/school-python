n = input().split()
s = set()
for x in n: 
    if x in s: 
        print('YES')
    else: 
        print("NO")
        s.add(x)
    