n = int(input())

s = {}
for x in range(n):
    inp = input()
    l = inp.lower()
    if l in s.keys():
        s[l].append(inp)
    else:
        s[l] = [inp]


inp = input().split()
c = 0
for x in inp:
    r = x.lower() in s.keys() and not x in s[x.lower()] or sum(a != b for a, b in zip(x, x.lower())) != 1
    if r :
        c+=1


print(c)
