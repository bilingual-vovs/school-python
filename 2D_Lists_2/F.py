n = int(input("N: "))
m = int(input("M: "))

lst = []
for x in range(n):
    lst.append(input().split())

i = int(input("I: "))
j = int(input("J: "))

def swap_columns(a, i, j):
    return [ [a[x][j] if y == i else a[x][i] if y == j else a[x][y] for y in range(m)]  for x in range(n) ]

for x in swap_columns(lst, i ,j):
    print(" ".join(x))