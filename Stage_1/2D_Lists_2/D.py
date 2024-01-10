n = int(input("N: "))

for x in range(n):
    y_list = []
    for y in range(n):
        y_list.append(str(abs(x-y)))
    print(' '.join(y_list))