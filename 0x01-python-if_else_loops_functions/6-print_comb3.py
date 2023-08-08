#!/usr/bin/python3
for number1 in range(10):
    for number2 in range(number1 + 1, 10):
        if number1 == 8 and number2 == 9:
            print(f"{number1}{number2}")
        else:
            print(f"{number1}{number2}", end=", ")
