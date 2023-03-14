#!/usr/bin/env python3

def main():
    MESSAGE = """
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
    """

    print(decode(MESSAGE))

def decode(text):
    ret_string = ""
    ind = 0

    for char in text:
        ascii_char = ord(char)

        if char.isupper():
            if ascii_char > ord('Z'):
                    ascii_char -= 26
            elif ascii_char < ord('A'):
                    ascii_char += 26

            text.replace(text[ind], chr(ascii_char))
            # ascii_char = chr(ord(char) + 2 % ord('Z'))

            # text = text.replace(text[ind], ascii_char)
        elif char.islower():
            if ascii_char > ord('z'):
                    ascii_char -= 26
            elif ascii_char < ord('a'):
                    ascii_char += 26

            text.replace(text[ind], chr(ascii_char))
            # ascii_char = chr(ord(char) + 2 % ord('z'))

        if char.isalpha():
            if ord(char) + 2 > ord('Z'):
                ret_string += (chr((ord(char) + 2 % ord('Z')) + ord('A')))
            else:
                ret_string += (chr(ord(char) + 2 % ord('Z')))
        else:
            ret_string += char
    ind += 1

    return ret_string

if __name__ == '__main__':
    main()
