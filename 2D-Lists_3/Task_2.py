inp = input()
yc = 9 - (98 - ord(inp[0])+7)
xc = 9 - int(inp[1])

for x in range(8):
    toPrint = []
    for y in range(8):
        if x+1 == xc and y+1 == yc:
            toPrint.append("K")
        elif abs(xc-(x+1)) == 2 and abs(yc-(y+1)) == 1 or abs(xc-(x+1)) == 1 and abs(yc-(y+1)) == 2:
            toPrint.append("*")
        else: 
            toPrint.append(".")
    print(' '.join(toPrint))