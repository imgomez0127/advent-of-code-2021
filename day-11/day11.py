"""
   Name    : day11.py
   Author  : Ian Gomez
   Date    : December 14, 2021
   Description :
   Github  : imgomez0127@github
"""

import numpy as np


def parse_input(file_name):
    with open(file_name, 'r') as f:
        return np.array([[int(c) for c in line.strip()] for line in f])


def solution(arr):
    flashes = 0
    first_synch = float('inf')
    for iteration in range(1000):
        arr += 1
        count_flashes = 0
        val = np.sum(arr > 9)
        flashed = set()
        while val != count_flashes:
            count_flashes = val
            for i in range(arr.shape[0]):
                for j in range(arr.shape[1]):
                    if arr[i, j] > 9 and (i, j) not in flashed:
                        arr[max(0, i-1):i+2, max(0, j-1):j+2] += 1
                        flashed.add((i, j))
            val = np.sum(arr > 9)
        cur_flashes = np.sum(arr > 9)
        if cur_flashes == arr.shape[0]*arr.shape[1]:
            first_synch = min(first_synch, iteration+1)
        flashes += cur_flashes
        arr[arr > 9] = 0
    return flashes, first_synch


def main():
    arr = parse_input('input.txt')
    print(solution(arr))

if __name__ == '__main__':
    main()
