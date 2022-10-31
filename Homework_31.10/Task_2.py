inp = input().split(" ")

s = 0
for x in inp: 
    if int(x) != abs(int(x)): 
        s+=int(x)
        
print(s)