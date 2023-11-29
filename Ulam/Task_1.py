n = int(input("n: "))
m = int(input("m: "))

x = [[0 for _ in range(n)] for _ in range(m)]
a, b, c, d = 0, m-1, 0, n-1
k = m * n

while k >= 1:
    for i in range(c, d + 1):
        x[a][i] = k
        k -= 1
    a += 1

    for i in range(a, b + 1):
        x[i][d] = k
        k -= 1
    d -= 1

    for i in range(d, c - 1, -1):
        x[b][i] = k
        k -= 1
    b -= 1

    for i in range(b, a - 1, -1):
        x[i][c] = k
        k -= 1
    c += 1


for row in x:
    for elem in row:
        print(f'{elem:3}', end=' ')
    print()