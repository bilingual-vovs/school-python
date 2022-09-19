a = int(input("Enter an 'a': "))
b = int(input("Enter a 'b': "))
n = int(input("Enter a 'n': "))

def solution(a, b, n):
    r = (a+b/100)*n
    return f"{int(r//1)} грн. {round(r%1*100)} коп."

print(solution(a, b, n))