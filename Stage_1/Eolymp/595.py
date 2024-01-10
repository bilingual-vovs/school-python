n = int(input())
cases = input().split(" ")
cases.insert(0, 0)
cases[1] = 0
cases[2] = int(cases[2])

for x in range(3, n+1): 
    cases[x] = int(cases[x]) + max((cases[x-2]), cases[x-3])

print(cases[-1])