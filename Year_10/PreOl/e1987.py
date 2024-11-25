n = input()

i = 1 
while n[-i] < n[-1-i]:
    i+=1

re = n[-1: -2-i: -1]
a = int(re[0])
j = +1
while a < int(n[-2-i]):
    a = int(re[j])
    j += 1

re1 = re[0: j-1]
re2 = re[j:]

r = n[0: -2-i]
print(r, a, re1, n[-2-i], re2)

    