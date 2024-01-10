comparationYear = 2025

print("Enter your date of birth:")
date = int(input())
age = comparationYear - date

if age != abs(age):
    print("You've born to late...")
    print("If you're dog, you'll be: " + str(age*7))
else:
    print("In " + str(comparationYear) + " you will be: " + str(age))
