"""
   Name    : day15.py
   Author  : Ian Gomez
   Date    : December 15, 2021
   Description : day 15 of advent of code using dijkstra's
   Github  : imgomez0127@github
"""

import collections
import heapq
import numpy as np

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parse_input(file_name):
    with open(file_name, 'r') as f:
        return np.array([[int(c) for c in line.strip()] for line in f])


def parse_input2(file_name):
    with open(file_name, 'r') as f:
        arr = np.array([[int(c) for c in line.strip()] for line in f])
    return np.vstack(
        [np.hstack([(arr+i+j) % 10 + (arr+i+j)//10 for j in range(5)])
         for i in range(5)])




def solution(arr):
    distances = collections.defaultdict(lambda: (float('inf'), None))
    distances[0, 0] = (0, None)
    priority_queue = [(0, (0, 0))]
    while priority_queue:
        cur_node = heapq.heappop(priority_queue)
        if cur_node[0] <= distances[cur_node[1]][0]:
            y1, x1 = cur_node[1]
            for (x2, y2) in directions:
                i = min(max(y1+y2, 0), arr.shape[0]-1)
                j = min(max(x1+x2, 0), arr.shape[1]-1)
                if cur_node[0]+arr[i, j] < distances[i, j][0]:
                    distances[i, j] = (cur_node[0]+arr[i, j], cur_node[1])
                    heapq.heappush(priority_queue,
                                   (cur_node[0]+arr[i, j], (i, j)))
    return distances[arr.shape[0]-1, arr.shape[1]-1]


def main():
    arr = parse_input('input.txt')
    print(solution(arr))
    arr2 = parse_input2('input.txt')
    print(arr2.shape)
    print(solution(arr2))

if __name__ == '__main__':
    main()
