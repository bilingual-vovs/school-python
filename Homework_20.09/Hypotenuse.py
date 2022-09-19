from math import sqrt
a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))

def solution(a, b):
    return sqrt(a**2 + b**2)

print(solution(a, b))