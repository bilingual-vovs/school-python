s = input().split()

ss = []
ssl = []

while len(s):
    l = [-100]
    i = 0
    while len(s) > i and int(l[-1]) < int(s[i]):
        l.append(s[i])
        i+=1
    l.pop(0)
    ss.append(l)
    ssl.append(len(l))
    s.pop(0)

print(' '.join(ss[ssl.index(max(ssl))]))