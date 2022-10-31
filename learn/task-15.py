greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings = [greeting[1] for greeting in greetings]
print(new_greetings)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newL = [num for num in digits if num%2==1]
print(newL)