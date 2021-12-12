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
            digits = filter(lambda x: x, [digit.strip() for digit in digits.split(' ')])
            numbers = filter(lambda x: x, [number.strip() for number in numbers.split(' ')])
            mat.append((list(digits), list(numbers)))
    return mat


def solution1(arr):
    cnt = collections.Counter()
    for _, numbers in arr:
        for number in numbers:
            cnt[len(number)] += 1
    return cnt[2]+cnt[3]+cnt[4]+cnt[7]


def string_to_signal(s):
    signal = 0
    for c in s:
        signal |= 1 << (ord(c)-ord('a'))
    return signal


def solution2(arr):
    solution = 0
    for (digits, numbers) in arr:
        # map proper letters to new signals
        signal_letter_map = {}
        # map signal representation to numbers
        number_map = {}
        # number to signal representation
        signal_map = {}
        # map signal to digit
        length_map = collections.defaultdict(list)
        for digit in digits:
            length_map[len(digit)].append(digit)
        number_map[string_to_signal(length_map[2][0])] = 1
        number_map[string_to_signal(length_map[3][0])] = 7
        number_map[string_to_signal(length_map[4][0])] = 4
        number_map[string_to_signal(length_map[7][0])] = 8
        signal_map[1] = string_to_signal(length_map[2][0])
        signal_map[7] = string_to_signal(length_map[3][0])
        signal_map[4] = string_to_signal(length_map[4][0])
        signal_map[8] = string_to_signal(length_map[7][0])
        signal_letter_map['a'] = signal_map[1] ^ signal_map[7]
        for number in length_map[6]:
            n = string_to_signal(number) ^ (signal_map[7] | signal_map[4])
            if bin(n).count("1") == 1:
                signal_map[9] = string_to_signal(number)
                number_map[string_to_signal(number)] = 9
                break
        signal_letter_map['g'] = signal_map[9] ^ (signal_map[7] | signal_map[4])
        signal_letter_map['e'] = signal_map[9] ^ signal_map[8]
        for number in length_map[6]:
            signal_num = string_to_signal(number)
            n = signal_num ^ signal_map[8]
            n2 = signal_num ^ signal_map[1]
            if bin(n).count("1") == 1 and bin(n2).count('1') != 4 and signal_num != signal_map[9]:
                signal_map[6] = signal_num
                number_map[signal_num] = 6
                break
        signal_letter_map['c'] = signal_map[6] ^ signal_map[8]
        signal_letter_map['f'] = signal_map[1] ^ signal_letter_map['c']
        off_3 = (signal_letter_map['a'] | signal_letter_map['c'] | signal_letter_map['f'] | signal_letter_map['g'])
        for number in length_map[5]:
            signal_num = string_to_signal(number)
            n = signal_num ^ off_3
            if bin(n).count("1") == 1:
                number_map[signal_num] = 3
                signal_map[3] = signal_num
                break
        signal_letter_map['d'] = off_3 ^ signal_map[3]
        signal_letter_map['b'] = (signal_map[1] | signal_letter_map['d']) ^ signal_map[4]
        five_signal = signal_letter_map['a'] ^ signal_letter_map['b'] ^ signal_letter_map['d'] ^ signal_letter_map['f'] ^ signal_letter_map['g']
        two_signal = signal_letter_map['a'] ^ signal_letter_map['c'] ^ signal_letter_map['d'] ^ signal_letter_map['e'] ^ signal_letter_map['g']
        zero_signal = signal_map[8] ^ signal_letter_map['d']
        number_map[five_signal] = 5
        number_map[two_signal] = 2
        number_map[zero_signal] = 0
        signal_map[5] = five_signal
        signal_map[2] = two_signal
        signal_map[0] = zero_signal
        number = int(''.join([str(number_map[string_to_signal(number)]) for number in numbers]))
        solution += number
    return solution


def main():
    arr = parse_input('real.txt')
    print(solution1(arr))
    print(solution2(arr))


if __name__ == '__main__':
    main()
