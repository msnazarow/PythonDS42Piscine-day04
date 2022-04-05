#!/usr/bin/python
import sys
from functools import reduce
from timeit import timeit


def loop(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum


def reducing(n):
    return reduce(lambda sum, x: sum + x ** 2, range(1, n + 1))


def main(args):
    if len(args) != 4:
        return
    functions = {
        'loop': loop,
        'reduce': reducing
    }
    try:
        operation, number, n = args[1], int(args[2]), int(args[3])
    except:
        print("Not valid input")
        return
    if operation not in functions:
        return

    print(timeit(lambda: functions[operation](n), number=number))


if __name__ == '__main__':
    main(sys.argv)
