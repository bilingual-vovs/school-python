n = input("Enter a number: ")
while not n.isnumeric():
    n = input("Enter a number(not string): ")
    
for p in n:
    print(p)

