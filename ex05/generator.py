#!/usr/bin/python
import sys

import psutil as psutil


def get_lines(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def main(args):
    if len(args) != 2:
        return
    try:
        lines = get_lines(args[1])
        for line in lines:
            pass
        process = psutil.Process()
        mem = process.memory_info().rss / (2 ** 30)
        cpu = process.cpu_times()
        print(f'Peak Memory Usage = {mem:.3f} Gb')
        print(f'User Time + System Time = {cpu.user + cpu.system:.2f}s')
    except:
        print("Error Occured")


if __name__ == '__main__':
    main(sys.argv)

