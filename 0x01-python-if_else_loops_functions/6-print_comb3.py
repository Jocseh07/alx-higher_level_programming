#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(number + 1, 10):
        if number == 0 and number2 == 9:
            print(f"{number}{number2}")
        else:
            print(f"{number}{number2}", end=", ")
