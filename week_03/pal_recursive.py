#!/usr/bin/env python3

def main():
    print(is_palindrome("121"))
    print(is_palindrome("görög"))
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("ab"))


def is_palindrome(text):
    if len(text) < 2:
        return True
    elif text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


if __name__ == '__main__':
    main()
