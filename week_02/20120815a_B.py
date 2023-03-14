#!/usr/bin/env python3

import sys

def main():
    n1 = request_number()
    n2 = request_number()

    print(sum_of_numbers(n1, n2))


def request_number():
    print("Please enter a number: ", end='')
    num = input()

    if num.isalpha():
        print("This is not a number or a valid number")
        request_number()

    if num.startswith('-'):
        if num[1:].isdigit():
            return int(num[1:])  * -1

        print("This is not a number or a valid number")
        request_number()

    return num

def sum_of_numbers(num1, num2):
    return int(num1) + int(num2)


if __name__ == '__main__':
    main()
