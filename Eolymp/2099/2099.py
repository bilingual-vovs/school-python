
input = open("./input.txt",  "r")
data = input.read()
ans = ""

d = data.split("\n")
a = d[1].split(' ')
b = set(d[3].split(" "))

for e in a:
    if not e in b:
        ans += str(e) + " "


an = open("output.txt", "w")
an.write(str(len(ans)/2) + "\n" + ans)