input = open("input.txt", "r").read()

x = input[0]
y = input[2]

input = input[4:]

m = [a.split(" ") for a in input.split("\n")]
res = "\n".join([" ".join([c[b] for c in reversed(m)]) for b in range(int(y))])

out = open("output.txt", "w")
out.write(y + " " + x + "\n" + res) 