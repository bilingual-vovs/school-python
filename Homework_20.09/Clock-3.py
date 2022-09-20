a = float(input("Enter an a: ")) 

def solution(a):
    s = a*1080/9
    m = s/60
    h = m/60
    return (int(h), int(m%60) , int(s%60))

print(solution(a))