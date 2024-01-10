inp = input().split(" ")

p = 0
n = 0
for x in inp: 
    if int(x) != abs(int(x)): 
        n +=1
    else:
        p+=1
        
print(f"Positive: {p}", f"Negative: {n}")