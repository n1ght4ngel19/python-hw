#!/usr/bin/env python3

import sys

def main():
    if not are_arguments_valid():
        return

    print(sum_of_numbers(sys.argv[1], sys.argv[2]))


def are_arguments_valid():
    if len(sys.argv) != 3:
        print("Error: You need to provide exactly two numbers")
        return False

    if sys.argv[1].isalpha() or sys.argv[2].isalpha():
        print("Error: You need to provide numbers only")
        return False

    if sys.argv[1].startswith('-'):
        if not (sys.argv[1][1:].isdigit()):
            print("Error: You need to provide numbers only")
            return False

        sys.argv[1] = int(sys.argv[1][1:]) * -1

    if sys.argv[2].startswith('-'):
        if not (sys.argv[2][1:].isdigit()):
            print("Error: You need to provide numbers only")
            return False

        sys.argv[2] = int(sys.argv[2][1:]) * -1

    return True

def sum_of_numbers(n1, n2):
    return int(n1) + int(n2)


if __name__ == '__main__':
    main()
