#!/usr/bin/env python3

def main():
    print("1-100-ig a számok összege: " + str(sum_of_nums_up_to(100)))


def sum_of_nums_up_to(num):
    return sum([num2 for num2 in range(num+1)])


if __name__ == '__main__':
    main()
