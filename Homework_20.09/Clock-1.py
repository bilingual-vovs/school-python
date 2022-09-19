h = int(input("Enter a h: "))
m = int(input("Enter a m: "))
s = int(input("Enter a s: "))

def solution(h, m, s):
    return ((h*60+m)*60+s)*360/43200

print(solution(h, m, s))