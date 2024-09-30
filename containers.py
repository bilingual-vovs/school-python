n = int(input())

c = [2, 3]

for x in range(2, n):
    c.append(c[-1]+c[-2])

print(c[-1])