n = int(input("Enter 'n': "))

def solution(n):
    a = n%10
    b = n//10%10
    c = n%1000//100
    return a + b + c

print(solution(n))