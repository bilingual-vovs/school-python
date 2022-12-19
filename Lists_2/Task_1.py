c = input().split()
p = 1
ph = int(input())
for x in c:
    if int(x) >= ph: p += 1
    # p += int(int(x)>=ph)
print(p)