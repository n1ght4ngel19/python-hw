#!/usr/bin/env python3

def main():
    url_string = "192.20.246.138:\n 6666"
    url_string_2 = "206.130.99.82:\n8080"

    print(clean_string(url_string))
    print(clean_string(url_string_2))
    print(clean_string("\n\n\n  \n   \ n\n\n\n\n\n\t   "))


def clean_string(s):
    for c in s:
        if c.isspace():
            s = s.replace(c, "")

    return s

if __name__ == '__main__':
    main()
