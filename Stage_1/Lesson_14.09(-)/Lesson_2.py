a = 2
b = 5


def space():
    print("\n" + "#" *30 +"\n")

operations = [a+b, a-b, a*b, a/b, a//b, a%b, a^b]

i = 0
for msg in operations:
    print(msg)
    i += 1
    if  i<len(operations):
        space()

#Comented
