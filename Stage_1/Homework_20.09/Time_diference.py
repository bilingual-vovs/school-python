h1 = int(input("Enter a h1: "))
m1 = int(input("Enter a m1: "))
s1 = int(input("Enter a s1: "))

h2 = int(input("Enter a h1: "))
m2 = int(input("Enter a m2: "))
s2 = int(input("Enter a s2: "))

def solution(h1, m1, s1, h2, m2, s2):
    return  (h2*60+m2)*60 + s2 - (h1*60+m1)*60 + s1

print(solution(h1, m1, s1, h2, m2, s2))