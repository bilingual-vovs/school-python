l = input().split()
s = set()
s2 = set()
r = 0
for x in l:
    if x in s:
        r += 1 
        s2.add(x)
    else: 
        s.add(x)

print(r + len(s2))