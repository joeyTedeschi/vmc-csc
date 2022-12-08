from math import sqrt
from random import choice


def squareRoot(num):
    return sqrt(num * 2)


def randomFromSeq(sequence):
    return choice(sequence)


num1 = int(input('Enter a number: '))
num2 = input(
    "Enter a second number, or 'skip' if you'd like to skip this number: ")

if num2 == 'skip':
    print(squareRoot(num1))
else:
    num2Int = int(num2)
    if num1 > num2Int:
        print(randomFromSeq(range(num2Int, num1 + 1)))
    elif num2Int > num1:
        print(randomFromSeq(range(num1, num2Int + 1)))
    else:
        print(num1)
