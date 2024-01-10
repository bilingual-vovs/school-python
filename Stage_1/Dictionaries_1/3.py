u = {232: 'Alice', 550: 'Bob', 190: 'Jack'}
i = [int(input()) for _ in range(4)]

for x in i:
    print(f'Hi, {u[x]}!') if x in u else print('Hi, to all!')
