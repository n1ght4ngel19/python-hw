#!/usr/bin/env python3

def main():
    draw_diamond(0)
    draw_diamond(1)
    draw_diamond(3)
    draw_diamond(4)
    draw_diamond(9)


def draw_diamond(height):
    if height % 2 != 1:
        print("Error: You need to provide an odd number! You provided: " + str(height))
        return -1

    print("Height is: " + str(height))
    to_draw = 1

    while to_draw < height:
        print(star_string(to_draw).center(height))
        to_draw += 2

    while to_draw != -1:
        print(star_string(to_draw).center(height))
        to_draw -= 2

    return height


def star_string(num):
    return "*" * num

if __name__ == '__main__':
    main()
