t = input().split()

w = {}
m, mf = 0, ""

for i in t:
    w[i] = w.get(i, 0) + 1
    if w[i] > m or (w[i] == m and i < mf):
        mf, m = i, w[i]

print(mf)