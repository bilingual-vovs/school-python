class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def DEPOSIT(self, data: list):
        name = data[0]
        sum = float(data[1])
        if name in self.clients: 
            self.clients[name] += sum
        else:
            self.clients[name] = sum
        print(f'{sum} added to {name}`s balance, now it`s {self.clients[name]}')

    def BALANCE(self, data: list):
        name = data[0]
        print(self.clients[name] if name in self.clients else 'Client not found')
    
    def TRANSFER(self, data: list):
        name = data[0]
        name2 = data[1]
        sum = float(data[2])

        if self.WITHDRAW([name, sum]):
            self.DEPOSIT([name2, sum])


    
    def INCOME(self, data: list):
        p = float(data[0])
        for x in self.clients:
            self.DEPOSIT([x, self.clients[x]/100*p])
        
    def WITHDRAW(self, data: list):
        name = data[0]
        sum = float(data[1])
        if (name in self.clients or print(f'Client not found')) and (self.clients[name] > sum or print(f'Not enought money on {name}`s balance, he hes only {self.clients[name]}')):
            self.clients[name] -= sum
            print(f'Now {name} have {self.clients[name]}')
            return True
        else:
            return False

    def listen(self):
        x = True
        print("Type 'exit' to close bank app")
        while x:
            print('>>>', end='')
            
            try:
                inp = input().split()
                op = inp[0]
            except:
                continue

            x = op != 'exit' 

            func = getattr(self, op, None)

            if func is not None and callable(func):
                func(inp[1:])
            else:
                print("There is no such operation")
                continue



monobank = Bank("Mono")

monobank.listen()