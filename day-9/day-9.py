"""
   Name    : day-9.py
   Author  : Ian Gomez
   Date    : December 9, 2021
   Description : Advent of code day 9 1-liner
   Github  : imgomez0127@github
"""

import numpy as np
import collections
import math
import sys
sys.setrecursionlimit(10000)

index_diffs = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])

def parse_file(file_name):
    with open(file_name, 'r') as f:
        return np.array([[int(c) for c in line.strip()] for line in f])

def get_lowpoint_indices(arr):
    return ((arr < np.vstack((np.full((1, arr.shape[1]), 10), arr[:-1]))) & (arr < np.vstack((arr[1:], np.full((1, arr.shape[1]), 10)))) & (arr < np.hstack((np.full((arr.shape[0], 1), 10), arr[:, :-1]))) & (arr < np.hstack((arr[:, 1:], np.full((arr.shape[0], 1), 10))))).nonzero()

def solution1(arr):
    return sum(map(lambda x: x+1, arr[(arr < np.vstack((np.full((1, arr.shape[1]), 10), arr[:-1]))) & (arr < np.vstack((arr[1:], np.full((1, arr.shape[1]), 10)))) & (arr < np.hstack((np.full((arr.shape[0], 1), 10), arr[:, :-1]))) & (arr < np.hstack((arr[:, 1:], np.full((arr.shape[0], 1), 10))))]))

def inbounds(indices, arr):
    return (len(list(filter(lambda x: x >= 0, indices))) ==
            len(list(filter(lambda x: x[0] < x[1], zip(indices, arr.shape)))) ==
            len(indices))

def bfs_helper(arr, lowpoint, basin):
    q = collections.deque([lowpoint])
    visited = set()
    while q:
        indices = q.popleft()
        ij = tuple(indices)
        visited.add(ij)
        for index_diff in index_diffs:
            if inbounds(indices+index_diff, arr):
                new_ij = tuple(indices+index_diff)
                if arr[new_ij] > arr[ij] and arr[new_ij] != 9:
                    basin[new_ij] |= True
                    if new_ij not in visited:
                        q.append(indices+index_diff)
    return basin

#Could optimize selecting top 3 basins by using quickselect
def solution2(arr, lowpoints):
    prod_arr = []
    for i, lowpoint in enumerate(lowpoints):
        basin = np.zeros(arr.shape).astype(bool)
        ij = tuple(lowpoint)
        basin[ij] = True
        basin = bfs_helper(arr, lowpoint, basin)
        prod_arr.append(np.sum(basin))
    return math.prod(sorted(prod_arr)[-3:])

# Could further optimize with quickselect but im lazy
def main():
    arr = parse_file('input.txt')
    print('Final Solution 1:', solution1(arr))
    lowpoints = np.array(list(zip(*get_lowpoint_indices(arr))))
    print('Final Solution 2:', solution2(arr, lowpoints))


if __name__ == '__main__':
    main()
