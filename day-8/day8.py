"""
   Name    : day8.py
   Author  : Ian Gomez
   Date    : December 11, 2021
   Description :
   Github  : imgomez0127@github
"""
import collections
def parse_input(file_name):
    mat = []
    with open(file_name, 'r') as f:
        for line in f:
            digits, numbers = line.split('|')
            digits = [digit.strip() for digit in digits.split(' ')]
            numbers = [number.strip() for number in numbers.split(' ')]
            mat.append((digits, numbers))
    return mat

def solution1(arr):
    cnt = collections.Counter()
    for _, numbers in arr:
        for number in numbers:
            cnt[len(number)] += 1
    return cnt[2]+cnt[3]+cnt[4]+cnt[7]

def main():
    arr = parse_input('real.txt')
    print(solution1(arr))


if __name__ == '__main__':
    main()
