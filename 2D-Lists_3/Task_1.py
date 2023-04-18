import re

n = int(input("N M: ").split()[0])

lst = []
for i in range(n):
    lst.append(input())

k = int(input("K: "))

for i in range(n):
    if len(re.findall("0" + " 0" * (k-1), lst[i])):
        print(i+1)
        break
