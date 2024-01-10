inp = input().split()
m = int(inp[0])
n = inp[1]


def recFunk(res = 0, i = 0):
    if i < len(n):
        recFunk(res + int(n[len(n) - i - 1])*m**i, i+1)
    else:
        print(res)

recFunk()