#!/usr/bin/env python3

import numpy as np


def parse_input(file_name):
    points = []
    is_point = True
    directions = []
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip() == '':
                is_point = False
                continue
            if is_point:
                x, y = line.strip().split(',')
                points.append((int(y), int(x)))
            else:
                _, position = line.strip().split('=')
                if 'x' in line:
                    directions.append((-1, int(position)))
                else:
                    directions.append((int(position), -1))
    max_row = max(points, key=lambda x: x[1])[1]+1
    max_col = max(points, key=lambda x: x[0])[0]+1
    arr = np.zeros((max_col, max_row)).astype(bool)
    for point in points:
        arr[point] = True
    return arr, directions


def print_arr(arr):
    for row in arr:
        for val in row:
            print('{}'.format('#' if val else '.'), end=' ')
        print('')


def solution(arr, directions):
    for (row, col) in directions:
        if col == -1:
            new_arr = np.array(arr[:row])
            for i in range(1, row+1):
                for j in range(new_arr.shape[1]):
                    new_arr[row-i, j] = arr[row-i, j] or arr[row+i, j]
            arr = new_arr
        else:
            new_arr = np.array(arr[:, :col])

            for i in range(new_arr.shape[0]):
                for j in range(1, col+1):
                    new_arr[i, col-j] = arr[i, col-j] or arr[i, col+j]
            arr = new_arr
    print_arr(arr)
    return np.sum(arr)


def main():
    arr, directions = parse_input('input.txt')
    print(solution(arr, directions))

if __name__ == '__main__':
    main()
