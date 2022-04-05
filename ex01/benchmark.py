#!/usr/bin/python
from timeit import timeit


def loop(emails):
    return list(_loop(emails))


def _loop(emails):
    for mail in emails:
        if mail[-9:] == "gmail.com":
            yield mail

def mapping(emails):
    return list(map(lambda mail: mail if mail.endswith("gmail.com") else None, emails))

def list_comp(emails):
    return [mail for mail in emails if mail.endswith("gmail.com")]


def main():
    better_loop = "It is better to use a loop"
    better_list_comp = "It is better to use a list comprehension"
    better_map = "It is better to use a map"
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    results = {
        better_loop: timeit(lambda: loop(emails), number=90000),
        better_map: timeit(lambda: mapping(emails), number=90000),
        better_list_comp:  timeit(lambda: list_comp(emails), number=90000)
    }
    results = sorted(results.items(), key=lambda x: x[1])
    print(results[0][0])
    print(f"{results[0][1]} vs {results[1][1]} vs {results[2][1]}")


if __name__ == '__main__':
    main()
