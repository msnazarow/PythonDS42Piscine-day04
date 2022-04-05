#!/usr/bin/python
from timeit import timeit


def loop(emails):
    return list(_loop(emails))


def _loop(emails):
    for mail in emails:
        if mail.endswith("gmail.com"):
            yield mail


def list_comp(emails):
    return [mail for mail in emails if mail.endswith("gmail.com")]


def main():
    better_loop = "It is better to use a loop"
    better_list_comp = "It is better to use a list comprehension"
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    results = {
        better_loop: timeit(lambda: loop(emails), number=900000),
        better_list_comp:  timeit(lambda: list_comp(emails), number=900000)
    }
    minimum = min(results.items())
    maximum = max(results.items())
    print(minimum[0])
    print(f"{minimum[1]} vs {maximum[1]}")


if __name__ == '__main__':
    main()
