# random password generator

import random
import string

def passwordGenerator():

    length = int(input("How long do you want your password to be?\n"))
    while length <= 0:
        length = int(input("Please enter a number greater than 0\n"))

    num_letters = int(input('How many of them are letters?\n'))

    while num_letters > length or num_letters < 0:
        num_letters = int(input("Out of bounds. Try again.\n"))

    letters = ''.join(random.choices(string.ascii_letters,k = num_letters))
    numbers = ''.join(random.choices(string.digits, k = length - num_letters))

    password = letters + numbers
    password = ''.join(random.sample(password, len(password)))

    print(password)



if __name__ == "__main__":
    passwordGenerator()
