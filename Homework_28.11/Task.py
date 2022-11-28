inp = [int(x) for x in input().split(" ")]

prev = 0
current = 1
max = 1
for x in inp:
    if x - prev == 1:
        current += 1
    else:
        if max < current:
            max = current
        current = 1
    prev = x

if max < current:
    max = current

print(max)