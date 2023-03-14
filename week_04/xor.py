#!/usr/bin/env python3

def main():
    print('1 XOR 1 is: ' + str(xor(1, 1)))
    print('1 XOR 0 is: ' + str(xor(1, 0)))
    print('0 XOR 0 is: ' + str(xor(0, 0)))
    print('0 XOR -1 is: ' + str(xor(0, -1)))
    print('None XOR  "python" is: ' + str(xor("python", None)))
    print('"python" XOR None is: ' + str(xor("python", None)))
    print('"python" XOR "python" is: ' + str(xor("python", "python")))
    print('None XOR None is: ' + str(xor(None, None)))


def xor(var1, var2):
    return (bool(var1) and not bool(var2)) or (bool(var2) and not bool(var1))


if __name__ == '__main__':
    main()
