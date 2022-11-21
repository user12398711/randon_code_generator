import string
import random

number = int(input("Enter number of password characters: "))
password = random.sample(string.printable, number)

print("Password is :")
print(str().join(password))
