n = int(input())
print("\n".join(["".join(["1" if y>x else "0" if y==x else "2" for y in range(n)]) for x in reversed(range(n)) ]))