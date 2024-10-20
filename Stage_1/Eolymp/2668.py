

def solution(n):
    arr = []

    for a in range(n):
        y_arr = []
        for b in range(n):
            y_arr.append(0)
        arr.append(y_arr)


    x = y = 0
    direction = 0
    
    def seter(x, y):
        arr[x][y] = 1

    def get(x, y):
        return arr[x][y]
     
    def fd():
        if direction == 0:
            seter(x+1, y)
            x = x + 1
        elif direction == 1:
            seter(x, y+1)
            y = y + 1
        elif direction == 2:
            seter(x-1 , y)
            x = x - 1
        elif direction == 3:
            seter(x, y-1)
            y = y - 1

    def pFd():
        if direction == 0 and x+2 < n:
            return True
        elif direction == 1 and y+2 < n:
            return True
        elif direction == 2 and x-2 >= n:
            return True
        elif direction == 3 and y-2 <= n:
            return True
        else:
            return False
    
    def rt():
        if direction == 3:
            direction = 0
        else:
            direction = direction + 1        

    seter(x, y)
    while True:
        if pFd():
            fd()
        else:
            rt()
            if pfd():
                break
    
    

solution(7)
