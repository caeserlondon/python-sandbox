"""Password generator"""
import random
import string
letters = list(string.ascii_lowercase)
numbers = list(string.digits)
# symbuls = list(string.punctuation)
symbols = ['!', '#', '$', '%', '&', '*', '+']
# print(letters)
# print(numbers)
# print(symbuls)
print("Wellcom to the password Generator")
num_letter = int(input("How many letter would you like in your password\n"))
num_number = int(input("How many numbers would you like in your password\n"))
num_symbols = int(input("How many symbols would you like in your password\n"))


letter = random.choices(letters, k=num_letter)
number = random.choices(numbers, k=num_number)
symbols = random.choices(symbols, k=num_symbols)

password = letter + number + symbols

random.shuffle(password)


print(f"your password is: {"".join(password)}")
