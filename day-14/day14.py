#!/usr/bin/env python3
import collections
import math


def parse_input(file_name):
    with open(file_name, 'r') as f:
        starting_compound = f.readline().strip()
        f.readline()
        reactions = {}
        for line in f:
           x, y = line.split('->')
           reactions[x.strip()] = y.strip()
    return starting_compound, reactions


def solution(starting_compound, reactions):
    initial_pairs = zip(starting_compound[:-1], starting_compound[1:])
    pair_counts = collections.Counter(map(lambda x: ''.join(x), initial_pairs))
    element_counts = collections.Counter()
    for _ in range(40):
        new_counts = collections.Counter()
        for pair, val in pair_counts.items():
            resulting_element = reactions[pair]
            pair1 = pair[0]+resulting_element
            pair2 = resulting_element+pair[1]
            new_counts[pair1] += val
            new_counts[pair2] += val
        pair_counts = new_counts
    for pair, val in pair_counts.items():
        for element in pair:
            element_counts[element] += val
    for element in element_counts:
        element_counts[element] = math.ceil(element_counts[element]/2)
    return max(element_counts.values())-min(element_counts.values())


def main():
    starting_compound, reactions = parse_input('input.txt')
    print(solution(starting_compound, reactions))


if __name__ == '__main__':
    main()
