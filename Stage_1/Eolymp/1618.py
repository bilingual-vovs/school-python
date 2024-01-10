input()
inp = [int(x) for x in input().split(" ")]
input()
inp2 = [int(x) for x in input().split(" ")]

prev = 10000000000
current = 0
max1 = 0
for x in inp:
    if x - prev == 1:
        current += 1
    else:
        if max1 < current:
            max1 = current
        current = 0
    prev = x

if max1 < current:
    max1 = current


prev2 = 1000000000
current2 = 0
max2 = 0
for x in inp2:
    if x - prev2 == 1:
        current2 += 1
    else:
        if max2 < current2:
            max2 = current2
        current2 = 0
    prev2 = x

if max2 < current2:
    max2 = current2

if max1 == max2:
    print(0)
else:
    print(max(max1, max2))
