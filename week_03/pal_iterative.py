#!/usr/bin/env python3

def main():
    print(is_palindrome("121"))
    print(is_palindrome("görög"))
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("ab"))


def is_palindrome(text):
    while len(text) > 1:
        if text[0]!= text[-1]:
            return False

        text = text[1:-1]

    return True


if __name__ == '__main__':
    main()
