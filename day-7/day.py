#!/usr/bin/env python3

def parse_input():
    with open('input.txt', 'r') as f:
        for line in f:
            return [int(num) for num in line.strip().split(',')]

def sum_rule(n):
    return (n*(n+1))/2

def bruteforce_sol(arr, gas_comp=lambda x: x):
    new_arr = []
    for i in range(max(arr)):
        cur_sum = 0
        for j in range(len(arr)):
            cur_sum += gas_comp(abs(i-arr[j]))
        new_arr.append(cur_sum)
    return min(new_arr)

def main():
    arr = parse_input()
    print(bruteforce_sol(arr))
    print(bruteforce_sol(arr, gas_comp=sum_rule))

if __name__ == '__main__':
    main()
