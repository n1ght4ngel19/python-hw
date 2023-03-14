#!/usr/bin/env python3

def main():
    print(is_palindrome("görög"))
    print(is_palindrome(""))
    print(is_palindrome("alma"))
    print(is_palindrome("121"))


def is_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    main()
