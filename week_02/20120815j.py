#!/usr/bin/env python3

def main():
    print("1977 -> " + reverse_number(1977))
    print("12568 -> " + reverse_number(12568))


def reverse_number(number):
    return str(number)[::-1]


if __name__ == '__main__':
    main()
