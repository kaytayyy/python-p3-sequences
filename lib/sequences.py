#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0, 1]
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        while len(fibonacci_list) < length:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        print("[{}]".format(", ".join(map(str, fibonacci_list))))

# print_fibonacci(0)
# print_fibonacci(1)
# print_fibonacci(2)
# print_fibonacci(3)
# print_fibonacci(8)