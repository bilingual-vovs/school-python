import math
n = int(input("N: "))

for x in range(n):
    y_list = []
    for y in range(n):
        y_list.append(str(math.ceil(int((y-(n-x))/(abs(y-(n-x)) or 1)+2/2))))
    print(' '.join(y_list))