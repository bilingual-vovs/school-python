def solution(n, m, x, y):
    if y%2 == 0:
        return y*m-1 - (m-x)
    else:
        return y*m-1 - x

