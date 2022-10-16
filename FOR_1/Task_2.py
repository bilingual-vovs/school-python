a = int(input("A: "))
b = int(input("B: "))
if a<b: 
    for x in range(a, b+1):
        print(x)
else:
    for x in reversed(range(b, a+1)):
        print(x)
