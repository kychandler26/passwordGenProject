import string
import random

# Ask the user for minimum number of characters required from the user
max_chars = int(input("What is the maximum number of characters allowed in the password?: "))

# Ask the user for maximum number of characters required from the user
max_chars = int(input("What is the minumum number of characters allowed in the password?: "))

# Ask the user if the password requires at least one upper case letter
upper_required = input("Does the password require at least one upper case letter (Y/N)?: ")

# Ask the user if the password requires at least one lower case letter
lower_required = input("Does the password require at least one lower case letter (Y/N)? ")

# Ask the user if the password requires at least one number
num_required = input("Does the password require at least one number (Y/N)? ")

# Ask the user if the password requires at least one special character (~!@#$%^&*()_+{}|:"<>?`-=[]\;',/")
special_char_required = input("Does the password require at least one special character?: ")

# Initialize the empty password string to append characters to so that password is formed
random_password = ""

# Initialize the set of all keyboard characters. This allows greater variation than using any of the sets alone and makes stronger passwords
keyboardCharacters = string.ascii_letters + string.digits + string.punctuation

counter = 0
while counter <= max_chars:
    new_char = ''.join(random.choices(keyboardCharacters))
    random_password = random_password + new_char
    counter += 1

print("Your randomly generated password is: ")
print(random_password)


