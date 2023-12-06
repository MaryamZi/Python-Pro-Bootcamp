import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

letter_count = int(input("How many letters would you like in your password? "))
symbol_count = int(input("How many symbols would you like? "))
number_count = int(input("How many numbers would you like? "))

password_list = []

for i in range(0, letter_count):
    password_list.append(random.choice(letters))

for i in range(0, symbol_count):
    password_list.append(random.choice(symbols))

for i in range(0, number_count):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Here is your password " + password)
