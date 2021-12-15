#!/usr/bin/env python3


class Node:

    def __init__(self, name, small, edges=None):
        self.name = name
        self.small = small
        self.edges = edges if edges else []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def build_graph(file_name):
    graph = {}
    with open(file_name, 'r') as f:
        for line in f:
            (start_name, end_name) = line.strip().split('-')
            if start_name in graph:
                start_node = graph[start_name]
            else:
                start_node = Node(start_name, start_name.islower())
                graph[start_name] = start_node
            if end_name in graph:
                end_node = graph[end_name]
            else:
                end_node = Node(end_name, end_name.islower())
                graph[end_name] = end_node
            start_node.edges.append(end_node)
            end_node.edges.append(start_node)
    return graph


def solution_helper(graph, cur, seen, returned=False):
    if cur.name == 'end':
        return 1
    if cur.small:
        seen.add(cur.name)
    paths = 0
    for node in cur.edges:
        if node.name == 'start':
            continue
        if node.name not in seen or not returned:
            new_returned = returned or node.name in seen
            paths += solution_helper(graph, node, set(seen),
                                     returned=new_returned)
    return paths


def solution(graph):
    paths = 0
    for node in graph['start'].edges:
        seen = {'start'}
        if node.small:
            seen.add(node.name)
        paths += solution_helper(graph, node, seen, returned=False)
    return paths


def main():
    graph = build_graph('input.txt')
    print(solution(graph))


if __name__ == '__main__':
    main()
