#!/usr/bin/env python3

DEEP_VOWELS = "aáoóuú"
HIGH_VOWELS = "eéiíöőüű"
DEEP = "Mély"
HIGH = "Magas"
MIXED = "Vegyes"
NEITHER = "Semmilyen"

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]

    for word in words:
        print(word + " -> " + hangrend_of(word))


def hangrend_of(str1):
    is_deep = False
    is_high = False

    for c in DEEP_VOWELS:
        if str1.find(c) != -1:
            is_deep = True

    for c in HIGH_VOWELS:
        if str1.find(c) != -1:
            is_high = True

    if is_deep and is_high:
        return MIXED
    elif is_deep:
        return DEEP
    elif is_high:
        return HIGH

    return NEITHER

if __name__ == '__main__':
    main()
