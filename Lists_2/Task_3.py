l = input().split()
lr = []

def isdefined(a,a2):
    if len(l) > a:
        return a
    else:
        return a2

for i in range(len(l)):
    if i%4 == 0 or i%4 == 1:
        lr.append(l[isdefined(i+2, i)])
    elif i%4 == 2 or i%4 == 3:
        lr.append(l[isdefined(i-2, i)])

print(lr)