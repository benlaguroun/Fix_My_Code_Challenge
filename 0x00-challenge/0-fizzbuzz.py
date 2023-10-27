#!/usr/bin/python3
"""
FizzBuzz Program
This Python script demonstrates the FizzBuzz problem. It prints numbers from 1 to a given number, following these rules:
- If a number is a multiple of 3, it prints "Fizz" instead.
- If a number is a multiple of 5, it prints "Buzz."
- If a number is both a multiple of 3 and 5, it prints "FizzBuzz."
"""

import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n following the FizzBuzz rules.
    Args:
    - n (int): The maximum number to print up to.
    """
    if n < 1:
        return

    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i) 
    print(" ".join(results))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
