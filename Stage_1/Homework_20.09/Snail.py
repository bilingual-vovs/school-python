from math import ceil 
h = int(input("Enter a 'h': "))
a = int(input("Enter an 'a': "))
b = int(input("Enter a 'b': "))

def solution(h, a, b):
    return ceil((h)/(a-b))

print(solution(h, a, b))