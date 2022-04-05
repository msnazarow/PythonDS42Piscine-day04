#!/usr/bin/python
import sys
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

def filtering(emails):
    return list(filter(lambda mail: mail.endswith("gmail.com"), emails))

def main(args):
    if len(args) != 3:
        return
    functions = {
        'loop' : loop,
        'list_comprehension': list_comp,
        'map': mapping,
        'filter': filtering
    }
    try:
        operation, number = args[1], int(args[2])
    except:
        print("Not valid input")
        return
    if operation not in functions:
        return
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    print(timeit(lambda : functions[operation](emails), number=number))


if __name__ == '__main__':
    main(sys.argv)
