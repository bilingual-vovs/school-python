p = float(input("Enter an p: ")) 
x = float(input("Enter an x: ")) 
y = float(input("Enter an y: ")) 

def solution(p, x, y):
    s = x + y/100
    r = s + p*s/100
    return (int(r), int(r%1*100))

print(solution(p, x, y))