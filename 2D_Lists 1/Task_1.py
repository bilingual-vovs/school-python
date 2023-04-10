count = int(input().split()[0])

list = []
for _ in range(count):
    list.append(input().split())

bx = 0
by = 0
y1 = 0
for y in list: 
    x1 = 0
    for x in y: 
        if int(x) > int(list[by][bx]):
            by = y1
            bx = x1
        x1+=1
    y1+=1 
        
print(bx, by)
