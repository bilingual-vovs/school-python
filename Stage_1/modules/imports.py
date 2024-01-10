def array2d(separator = ' '):
    n, m = input().split(separator)
    out = []
    for _ in range(int(n)):
        out.append(input().split(separator)[0,int(m)])
    return out