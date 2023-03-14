#!/usr/bin/env python3

def main():
    print(product([]))
    print(product([1, 2, 3, 4, 5]))
    print(product([-1, -2, -3, -4, -5]))
    print(product([1, 2, 3, 4, 0]))


def product(numbers):
    if len(numbers) == 0:
        return 1
    else:
        prod = numbers[0]

        for item in numbers[1:]:
            prod *= item

        return prod


if __name__ == '__main__':
    main()
