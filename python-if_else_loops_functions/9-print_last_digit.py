#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("Last digit of {} is {}".format(number, last_digit))
    return last_digit
