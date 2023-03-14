#!/usr/bin/env python3

def main():
    diff = diff_of_sumsquare_sqauresum_up_to(100)

    print("""Az első száz természetes szám összegének a négyzete
és az első száz természetes szám négyzetösszege közti
különbség: """ + str(diff))


def sum_of_squares_up_to(num):
    return sum(pow(n, 2) for n in range(num+1))


def square_of_sums_up_to(num):
    return pow(sum(n for n in range(num+1)), 2)


def diff_of_sumsquare_sqauresum_up_to(num):
    sum_num = sum_of_squares_up_to(num)
    sqare_num = square_of_sums_up_to(num)

    return sqare_num - sum_num


if __name__ == '__main__':
    main()
