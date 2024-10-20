def printSpace():
    print("\n" + "#" *30 +"\n")

def patternPrint(pattern, ending):
    if not ending:
        ending = ""
    elif ending == True:
        ending = pattern[0]
    print(pattern * 20 + ending)
print("Hello world")

printSpace()


print("Multiplyed hello:")


print("Hello" *5)


printSpace()

print("|-|-" * 20 + "|")
patternPrint("*-", True)
patternPrint("+**", True)

printSpace()

patternPrint("|l1l", True)
