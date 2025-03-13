# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *
import re
from collections import defaultdict
from itertools import combinations

year, day = '2024', '23'


def both_connected(connections, l, r):
    return (l, r) in connections or (r, l) in connections


def is_clique(graph, nodes):
    # Check if all nodes in the subset are connected to each other
    return all(graph[a].intersection(nodes) == nodes - {a} for a in nodes)


def bron_kerbosch(graph, result, nodes, exlusions, cliques):
    if not nodes and not exlusions:
        cliques.append(result)
        return
    for node in list(nodes):
        bron_kerbosch(
            graph,
            result.union({node}),
            nodes.intersection(graph[node]),
            exlusions.intersection(graph[node]),
            cliques,
        )
        nodes.remove(node)
        exlusions.add(node)


def largest_clique(graph):
    nodes = set(graph.keys())
    cliques = []
    bron_kerbosch(graph, set(), nodes, set(), cliques)
    return max(cliques, key=len) if cliques else set()


def solve():
    puzzle = load_input(test=False)
    graph = defaultdict(set)
    
    computers = set(re.findall(r'([a-z]+)', puzzle))
    connections = re.findall(r'([a-z]+)-([a-z]+)', puzzle)
    
    # create graph
    for pc in computers:
        graph[pc] = {a if b == pc else b for a, b in connections if pc in (a, b)}
    
    triples = set()
    for k, v in graph.items():
        if k.startswith('t'):
            for c in combinations(v, 2):
                if both_connected(connections, *c):
                    triples.add(tuple(sorted((k, *c))))
    
    part1 = len(triples)
    part2 = ','.join(sorted(largest_clique(graph)))
    
    return part1, part2


#  ----------   Start   ----------   #

run_puzzle(day, year, solve)
