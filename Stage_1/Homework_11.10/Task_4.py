a = int(input("Enter 'A': "))
b = int(input("Enter 'B': "))

for x in range((a//5+1)*5, b, 5):
    print(x)