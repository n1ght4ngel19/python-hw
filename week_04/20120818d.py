#!/usr/bin/env python3

def main():
    print("1. feladat")
    words = ['auto', 'villamos', 'metro']
    words_upper = [word.upper() + "!" for word in words]
    print(str(words) + " -> " + str(words_upper))
    print_line(30)


    print("2. feladat")
    names = ['aladar', 'bela', 'cecil']
    names_capital = [name.capitalize() for name in names]
    print(str(names) + " -> " + str(names_capital))
    print_line(30)


    print("3. feladat")
    zero_list = [0 for i in range(10)]
    print(zero_list)
    print_line(30)


    print("4. feladat")
    nums = [num for num in range(1, 10+1)]
    nums_double = [num * 2 for num in nums]
    print(str(nums) + " -> " + str(nums_double))
    print_line(30)


    print("5. feladat")
    nums_str = [str(num) for num in range(1, 10+1)]
    nums_num = [int(num) for num in nums_str]
    print(str(nums_str) + " -> " + str(nums_num))
    print_line(30)


    print("6. feladat")
    num_str = "1234567"
    nums_lst = [int(num) for num in list(num_str)]
    print(num_str + " -> " + str(nums_lst))
    print_line(30)


    print("7. feladat")
    fox_string = 'The quick brown fox jumps over the lazy dog'
    fox_string_word_lengths = [len(word) for word in fox_string.split()]
    print(fox_string + " -> " + str(fox_string_word_lengths))
    print_line(30)


    print("8. feladat")
    python_string = 'python is an awesome language'
    python_string_first_letters = [word[0] for word in python_string.split()]
    print(python_string + " -> " + str(python_string_first_letters))
    print_line(30)


    print("9. feladat")
    fox_tuple_list = [(word, len(word)) for word in fox_string.split()]
    print(fox_string + " -> " + str(fox_tuple_list))
    print_line(30)


    print("10. feladat")
    less_than_ten_even = [num for num in range(10+1) if num % 2 == 0]
    print(str(less_than_ten_even))
    print_line(30)


    print("11. feladat")
    less_than_twenty = [pow(num, 2) for num in range(20) if pow(num, 2) % 2 == 0]
    print(str(less_than_twenty))
    print_line(30)


    print("12. feladat")
    less_than_twenty_last_is_four = [pow(num, 2) for num in range(20) \
        if pow(num, 2) % 2 == 0 \
        and str(pow(num, 2)).endswith("4")]
    print(str(less_than_twenty_last_is_four))
    print_line(30)


    print("13. feladat")
    upper_abc = "".join([chr(num) for num in range(65, 90+1)])
    print(upper_abc)
    print_line(30)


    print("14. feladat")
    fruits = ['  apple  ', '  banana  ', '  kiwi  ']
    fruits_stripped = [word.strip() for word in fruits]
    print(str(fruits) + " -> " + str(fruits_stripped))
    print_line(30)


    print("15. feladat")
    binary = [1, 0, 1, 1, 0, 1, 0, 0]
    binary_string = "".join([str(digit) for digit in binary])
    print(str(binary) + " -> " + binary_string)
    print_line(30)


def print_line(num):
    print("-" * num)

if __name__ == '__main__':
    main()
