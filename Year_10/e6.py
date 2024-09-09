n = int(input())

l = []
for i in range(n):
    l.append([int(x) for x in input().split()][::-1])



l.sort()
x = [l[i][0]*(l[1][1]-i) for i in range(n:x-1)]

print(sum(x))