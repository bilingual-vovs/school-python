n = int(input())
s = {}
for _ in range(n):
    a,b = input().split()
    s[a] = b
    s[b] = a
print(s[input()])
