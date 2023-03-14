#!/usr/bin/env python3

def main():
    print("1-100-ig a számok számjegyeinek összege: " + str(sum_of_digits_up_to(100)))


def sum_of_digits_up_to(num):
    num_digits_sum = 0

    for num in range(num+1):
        current_digits_sum = sum(int(digit) for digit in list(str(num)))
        num_digits_sum += current_digits_sum

    return(num_digits_sum)


if __name__ == '__main__':
    main()
