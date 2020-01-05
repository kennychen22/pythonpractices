#!/usr/bin/env python3

#exercise 9
import random as rand
import os
print (os.getcwd())

number = int(rand.randint(1, 10))
print(number)

guess = int(input("Guess a number between 1 - 9\n"))
count = 1

while(guess != number):
    guess = int(input("Oops, try again!"))
    count = count + 1




print("You win!")
print('It took you ' + str(count) + ' guesses.')
