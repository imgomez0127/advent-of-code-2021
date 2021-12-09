#!/usr/bin/env python3

import numpy as np

def parse_file(file_name):
    with open(file_name, 'r') as f:
        return np.array([[int(c) for c in line.strip()] for line in f])


def solution(arr):
    return sum(map(lambda x: x+1, arr[(arr < np.vstack((np.full((1, arr.shape[1]), 10), arr[:-1]))) & (arr < np.vstack((arr[1:], np.full((1, arr.shape[1]), 10)))) & (arr < np.hstack((np.full((arr.shape[0], 1), 10), arr[:, :-1]))) & (arr < np.hstack((arr[:, 1:], np.full((arr.shape[0], 1), 10))))]))


def main():
    arr = parse_file('input.txt')
    print(arr)
    print(solution(arr))


if __name__ == '__main__':
    main()
