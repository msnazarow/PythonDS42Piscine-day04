#!/usr/bin/python
import sys
from collections import Counter
from functools import reduce
from random import randint
from timeit import timeit


def loop(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum


def dict_count(randoms):
    randoms_dict = {}
    for elem in randoms:
        if randoms_dict.get(elem):
            randoms_dict[elem] += 1
        else:
            randoms_dict[elem] = 1
    return randoms_dict

def most_common(randoms, n):
    randoms_dict = dict_count(randoms)
    return dict(sorted(randoms_dict.items(), key=lambda x: x[1], reverse=True)[:n])

def main():
    randoms = [randint(0, 100) for i in range(1000000)]
    print(f"My Function: {timeit(lambda: dict_count(randoms), number=1)}")
    print(f"Counter: {timeit(lambda: Counter(randoms), number=1)}")
    print(f"My Top: {timeit(lambda: most_common(randoms, 10), number=1)}")
    print(f"Counter's Top: {timeit(lambda: Counter(randoms).most_common(10), number=1)}")

if __name__ == '__main__':
    main()
