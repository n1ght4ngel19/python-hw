#!/usr/bin/env python3

def main():
    print(number_of_digits(2, 256))


def number_of_digits(number, power):
    return len(str(number ** power))


if __name__ == '__main__':
    main()
