a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
x = int(input("Enter x2: "))
y = int(input("Enter y2: "))

if abs(a - x) <= 1 and (b - y) <= 1: 
    print("Yes")
else:
    print("No")