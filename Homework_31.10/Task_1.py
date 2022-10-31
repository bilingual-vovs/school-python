inp = input().split(" ")

s = 0
for x in inp: 
    if int(x)%3 == 0: 
        s+=int(x)
        
print(s)