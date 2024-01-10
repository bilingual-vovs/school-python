from re import split
input = split(r'[ \n]', open("input.txt", "r").read())

x1 = int(input[1])
r1 = int(input[-4])
c1 = int(input[-3])
r2 = int(input[-2])
c2 = int(input[-1])

out = open("output.txt", "w")
out.write(str(sum([int(input[x*x1+y+2]) for y in range(c1-1, c2) for x in range(r1-1, r2)])))