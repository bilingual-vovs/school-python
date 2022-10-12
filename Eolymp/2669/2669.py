input = input()

x = int(input[0])
y = int(input[2])

m = []
for _ in range(x):
    a = str(input())
    print(str(a))
    m.append(a)

res = "\n".join([" ".join([c[b] for c in reversed(m)]) for b in range(y)])

print(y + " " + x + "\n" + res) 