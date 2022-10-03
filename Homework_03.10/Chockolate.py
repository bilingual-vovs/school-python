n = int(input("Enter n: "))
m = int(input("Enter m: "))
k = int(input("Enter k: "))

if k% m == 0 or k%n == 0:
    print("YES")
else:
    print("NO")