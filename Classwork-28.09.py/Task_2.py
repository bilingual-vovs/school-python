a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
x = int(input("Enter x2: "))
y = int(input("Enter y2: "))

if a==x or y==b or abs(a-x) == abs(b-y): 
    print("Yes")
else:
    print("No")