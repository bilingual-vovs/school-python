inp = input().split()
n = int(inp[0])
m = int(inp[1])

list = []
for x in range(n):
    sublist = []
    for y in range(m):
        if x%2 == y%2:
            sublist.append("*")
        else:
            sublist.append(".")
    print("".join(sublist))
    list.append(sublist)

print(list)