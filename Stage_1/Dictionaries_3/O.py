
class File: 
    def __init__(self, flags):
        self.flags = flags
    
    def __getitem__(self, key):
        return key in self.flags

files = {}

def create_file(data):
    files[data[0]] = File(data[1:])

def run(cmd: str):
    cmds = {
        'read': 'R',
        'execute': "X",
        'write': 'W'
    }
    action = cmd.split()
    return files[action[1]][cmds[action[0]]]

n = int(input())


for _ in range(n):
    create_file(input().split())

m = int(input())

stack = []

for _ in range(m):
    stack.append(input())

for cmd in stack:
    print("OK" if run(cmd) else "Access denied")