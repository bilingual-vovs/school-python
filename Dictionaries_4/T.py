n = int(input())

s = {}
for x in range(n):
    inp = input()
    s[inp.lower] = inp

inp = input().split()
c = 0
for x in inp:
    r = False
    try:
        print(s[x.lower()])
        r = s[x.lower()] != x
    except:
        continue 
    if  r :
        c+=1

print(c)

