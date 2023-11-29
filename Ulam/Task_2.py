import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("n: "))
m = int(input("m: "))

x = [['*' if is_prime(i) else '_' for i in range(n)] for _ in range(m)]
a, b, c, d = 0, m-1, 0, n-1
k = m * n

while k >= 1:
    for i in range(c, d + 1):
        x[a][i] = '*' if is_prime(k) else '_'
        k -= 1
    a += 1

    for i in range(a, b + 1):
        x[i][d] = '*' if is_prime(k) else '_'
        k -= 1
    d -= 1

    for i in range(d, c - 1, -1):
        x[b][i] = '*' if is_prime(k) else '_'
        k -= 1
    b -= 1

    for i in range(b, a - 1, -1):
        x[i][c] = '*' if is_prime(k) else '_'
        k -= 1
    c += 1


for row in x:
    for elem in row:
        print(elem, end=' ')
    print()