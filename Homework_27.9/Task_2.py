from cmath import pi


a = int(input("A: "))
b = int(input("B: "))

if pi*(a**2) > b**2:
    print("Сircle")
else: 
    print("Squere")