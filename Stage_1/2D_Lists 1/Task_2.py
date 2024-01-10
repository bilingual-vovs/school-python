n = int(input())

list = []
for x in range(n):
    sublist = []
    for y in range(n):
        if x == y or n-x-1==x or n-y-1==y or n-y-1 == x:
            sublist.append("*")
        else:
            sublist.append(".")
    print("".join(sublist))
    list.append(sublist)

print(list)