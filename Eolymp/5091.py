n = int(input())

y = 1
y2 = 1
for _ in range(n):
    yp = y
    y+=y2
    y2 = yp

print(y)