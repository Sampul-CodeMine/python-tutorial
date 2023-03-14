#!/usr/bin/python3
# Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
# Write your program below


number = 0
while True:
    try:
        number = int(input("Enter Number: "))
        break
    except:
        print("Numeric value required.")
if number == 0:
    print(f"{number:d} is zero")
elif number < 0:
    print(f"{number:d} is Negative.")
else:
    print(f"{number:d} is Positive.")
