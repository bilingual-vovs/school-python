n = int(input())

def hanoi(a, b, c, n):
    if n > 0:
        hanoi(a,c, b,n-1)
        print(a, b)
        hanoi(c,b,a,n-1)

hanoi(1, 2, 3, n)