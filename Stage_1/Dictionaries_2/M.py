c = {}

while True:
    try:
        l = input().split()
        a, v = l[0], int(l[1])

        if a in c:
            c[a] += v
        else:
            c[a] = v
    except IndexError:
        break

for a in sorted(c.keys()):
    print(a, c[a])
