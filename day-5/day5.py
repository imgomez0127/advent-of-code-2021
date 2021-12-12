"""
   Name    : day5.py
   Author  : Ian Gomez
   Date    : December 10, 2021
   Description :
   Github  : imgomez0127@github
"""
import itertools
import numpy as np

def parse_file(file_name):
    with open(file_name, 'r') as f:
        return [[tuple((int(c) for c in pair.strip().split(',')))
                 for pair in line.strip().split('->')] for line in f]

def compute_vals(lines):
    max_row = max(itertools.chain.from_iterable(lines), key=lambda x: x[0])[0]
    max_col = max(itertools.chain.from_iterable(lines), key=lambda x: x[1])[1]
    arr = np.zeros((max_row+1, max_col+1))
    for (y1, x1), (y2, x2) in lines:
        if x1 == x2 or y1 == y2:
            arr[min(x1, x2):max(x1, x2)+1, min(y1, y2):max(y1, y2)+1] += 1
    return np.sum(arr >= 2)

def compute_vals2(lines):
    max_row = max(itertools.chain.from_iterable(lines), key=lambda x: x[0])[0]
    max_col = max(itertools.chain.from_iterable(lines), key=lambda x: x[1])[1]
    arr = np.zeros((max_row+1, max_col+1))
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2 or y1 == y2:
            arr[min(y1, y2):max(y1, y2)+1, min(x1, x2):max(x1, x2)+1] += 1
        else:
            iter1 = range(y1, y2+1) if y1 < y2 else reversed(range(y2, y1+1))
            iter2 = range(x1, x2+1) if x1 < x2 else reversed(range(x2, x1+1))
            for (y, x) in zip(iter1, iter2):
                arr[y, x] += 1
    return np.sum(arr >= 2)

def main():
    lines = parse_file('input.txt')
    print(compute_vals(lines))
    print(compute_vals2(lines))

if __name__ == '__main__':
    main()
