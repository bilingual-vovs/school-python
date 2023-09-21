
n, m = input().split()
maxMax = 0
ans = ''
x = 0
for _ in range(int(n)):
   x+=1
   a = sum([int(x) for x in input().split()]) 
   if a > maxMax:
      maxMax = a
      ans = str(x)
   elif a == maxMax:
      ans += ' ' + str(x)

print(ans)