n = int(input())

l = [[] for _ in range(n)]
for y in range(n):
    inp = input().split()
    for x in range(n):
        if inp[x] == '1':
            l[y].append(str(x+1))
    
for x in l:
    print(len(x), " ".join(x))
