#!/usr/bin/python3
# Write a program that generates a random number between 1 and 100 and asks the user to guess the number.
# The program should keep asking the user to guess until they get the number right, and then print out
# the number of guesses it took.
# Write your program below

import random

g_range = random.randint(1, 100)
is_found = False
counter = 0

while is_found is False:
    while True:
        num_val = input("Guess Number: ( {} - {} ) ".format(1, 100))
        counter += 1
        if num_val.isnumeric():
            num_val = int(num_val)
            if num_val > g_range:
                is_found = False
                print("{} is bigger than the number to guess.".format(num_val))
                continue
            elif num_val < g_range:
                is_found = False
                print("{} is smaller than the number to guess.".format(num_val))
                continue
            else:
                is_found = True
                break

        else:
            is_found = False
            print("Must be numeric data.")
            continue


if is_found is True and counter <= 5:
    print("You are a genius. You found the number to guess '{}' after {} guesses.".format(g_range, counter))
elif is_found is True and counter <=10:
    print("Nice work. You found the number to guess '{}' after {} guesses.".format(g_range, counter))
else:
    print("You found the number to guess {} after {} guesses. Your attempt was poor.".format(g_range, counter))
exit(0)