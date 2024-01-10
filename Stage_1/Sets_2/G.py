n = int(input())

r = set(str(x) for x in range(n))
x = False
inp = -1
ans = "NO"
while x != 'HELP':
    x = input()
    if x == "YES":
        r = r.intersection(inp)
    elif x == 'NO':
        r = r.difference(inp)
    else:
        inp = set(x.split())

print(' '.join(sorted(r)))