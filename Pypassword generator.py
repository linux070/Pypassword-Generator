# `````````` Building a Pypassword Generator Project! ``````

print("Welcome to the Pypassword Generator!\n")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_list = []
# looping through the data available and adding the password char to it.
for x in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for x in range(1, nr_symbols + 1):
   password_list += random.choice(symbols)

for x in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# print(password_list) ---- just dey play😂😂.

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""     # --- (this is another empty list).
#`````` Now we have to shuffle your password to make it more unique.``````
random.shuffle(password_list) 
for char in password_list:
    password += char
print(f"Your generated password is : {password}")


# `````` linuxmode ````````