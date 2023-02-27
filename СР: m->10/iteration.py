inp = input().split()
m = int(inp[0])

res = 0
i = 0
for s in reversed(inp[1]):
    res += int(s)*m**i
    i+=1
print(res)