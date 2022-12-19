l = input().split()

inMin = 0
inMax = 0
for x in range(len(l)):
    l[x] = int(l[x])
    if l[x] > l[inMax]:
        inMax = x
    elif l[x] < l[inMin]: 
        inMin = x
    
a = l[inMin]
l[inMin] = l[inMax]
l[inMax] = a 
print(l)