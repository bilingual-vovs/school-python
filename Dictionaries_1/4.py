i = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
print("Equipment:")
for k, v in i.items():
    print(f"{v} {k}")
print(f"Total number of things: {sum(i.values())}")
