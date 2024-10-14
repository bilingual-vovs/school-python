n = int(input())


def maxRows(n):
    s = 0
    i = 0
    while s < n:
        i+=1
        s+=i
    return i 

def sumRows(r):

    s = 0
    for x in range(r):
        s += x+1
    return s

    for x in range(maxRows(n), b):
        v += next(n, x)

v = []

mn = maxRows(n)
mx = n

for x in range(mn, mx):
    l = [0 for _ in range(mn)]
    l[0] = x

print(s)