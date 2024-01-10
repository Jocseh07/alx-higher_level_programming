#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_to_int:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    romans = list(roman.keys())
    romann = list(roman.values())
    numbers = []
    number = 0
    for a in roman_string:
        numbers.append(romann[romans.index(a)])
    sortedNumbers = sorted(numbers, reverse=True)
    for n in sortedNumbers:
        if sortedNumbers.index(n) <= numbers.index(n):
            number += n
        elif sortedNumbers.index(n) > numbers.index(n):
            number -= n
    if number > 3999:
        return 0
    return number
