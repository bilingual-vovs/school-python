clas = input().split(" ")
position = 1
petro = int(input())
for x in clas:
    if int(x) >= petro: position += 1
    # p += int(int(x)>=ph)
print(position)