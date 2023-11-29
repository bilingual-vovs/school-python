inp = input().split()

w = {}
r = ''
for x in inp:
    if x in w:
        w[x] += 1
    else:
        w[x] = 1
    r += str(w[x]-1) + ' '
print(r)