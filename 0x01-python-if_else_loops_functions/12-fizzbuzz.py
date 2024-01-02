#!/usr/bin/python3


def fizzbuzz():
    for number in range(0, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(f"{number:d}", end="")
