#!/usr/bin/python3
def fizzbuzz():
    for h in range(1, 101):
        if h % 15 == 0:
            print("FizzBuzz", end=" ")
        elif h % 5 == 0:
            print("Buzz", end=" ")
        elif h % 3 == 0:
            print("Fizz", end=" ")
        else:
            print('{}'.format(h), end=" ")
