
s = {}

def f(r, d):
    if r in d.keys():
        return d[r]
    else:
        return False 

for x in range(6):
    inp = input().split()
    n = inp[0]
    e = inp[1]
    a = inp[2]
    if n in s.keys():
        s[n] = (f(e, s[n]) or {}) + int(a)
    else:
        s[n] = {}
        s[n][e] = int(a)

for x in s.keys():
    print(x + ":")
    for y in s[x].keys():
        print(f'{y} {s[x][y]}')